# Download Packages

import cv2
import os
import numpy as np
from PIL import Image
from tqdm import tqdm

## MT Dataset 사용

img_pth = 'images/makeup/'
mask_pth = 'segs/makeup/'
lips_img_pth = 'images/makeup_lips/'
lips_mask_pth = 'segs/makeup_lips/'

#os.mkdir(lips_img_pth)
#os.mkdir(lips_mask_pth)

## Image & Masking Image shape 확인
## Image와 Masking Image를 결합하기 위해서는 Image Size 조정 필요

cv2.imread(os.path.join(img_pth, (os.listdir(img_pth)[0]))).shape
#(361, 361, 3)

cv2.imread(os.path.join(mask_pth, (os.listdir(mask_pth)[0]))).shape
#(321, 321, 3)

## Lip Masking Image 학습

for img_name in tqdm(os.listdir(img_pth)):
    mask = cv2.imread(os.path.join(mask_pth, img_name), 0)
    mask = mask.flatten()
    lips = np.zeros(321*321)
		## class 7: upper-lip / class 9: lower-lip
    lips_loc = (np.where((mask==7)|(mask==9))[0]).tolist()
    for loc in lips_loc:
        lips[loc] = 200
    cv2.imwrite(os.path.join(lips_mask_pth, img_name), np.reshape(lips, (321, 321)))

## Lip component Image 학습

for img_name in tqdm(os.listdir(img_pth)):
    
    mask = cv2.imread(os.path.join(mask_pth, img_name), 0)
    mask = mask.flatten()
    
    # img = cv2.imread(os.path.join(img_dir, img_name))
    img = Image.open(os.path.join(img_pth, img_name))
		# img size 변경
    img = np.array(img.resize((321,321)))
    img = np.array(img)
    img = np.reshape(img, (321*321, 3))
    
    lips_img = np.zeros((321*321,3))
    lips_loc = (np.where((mask==7)|(mask==9))[0]).tolist()
    for loc in lips_loc:
				# cv2: BGR / numpy: RGB
        lips_img[loc, 0] = img[loc, 2]
        lips_img[loc, 1] = img[loc, 1]
        lips_img[loc, 2] = img[loc, 0]
    cv2.imwrite(os.path.join(lips_img_pth, img_name), np.reshape(lips_img, (321, 321, 3)))
