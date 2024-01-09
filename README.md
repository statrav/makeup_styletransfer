# Makeup Transfer 연구보고서

### 개요

1. 연구주제
    - CLIPstyler를 활용한 Makeup Transfer
    
2. 연구분야
    - GAN(Generative Adversarial Network)
    - Style Transfer
    - Makeup Transfer
    
3. 연구목적
    - CLIP모델을 활용한 국소적인 Makeup Transfer의 시도는 하나의 이미지를 투입하여 Makeup Image의 다양성을 표현할 수 있게 만들기에, Personal Makeup 시장에서의 활용성 향상에 영향을 준다
    
4. 연구배경
    - 꾸준히 증가하는 Makeup Market 규모
    - Personal Makeup Finder의 증가
    - Facial에 국한하는 Style Transfer의 특이성
    
5. 진행기간
    - 2022년 12월 ~ 2023년 02월 (약 3개월)

### 연구내용

1. 주요 참고논문
    - Spatially-Invariant Style-Codes Controlled Makeup Transfer, CVPR, 2021
    - BeautyGAN : Instance-level Facial Makeup Transfer with Deep Generative Adversarial Network, ACM MM, 2018
    - Lipstick ain’t enough : Beyond Color Matching for In-the-Wild Makeup Transfer, CVPR, 2021
    - Unpaired Image-to-Image Translation Using Cycle-Consistent Adversarial Network, ICCV, 2017
    - CLIPstyler : Image Style Transfer with a Single Text Condition, CVPR, 2022
    - Analyzing and Improving the Image Quality of StyleGAN, CVPR, 2020

1. 주요 아이디어
    - CLIPstyler model + MakeupTransfer model

1. Dataset
    - MT(MakeupTransfer)-Dataset
    - CPM Dataset

1. 연구 진행
    - makeupCLIP 가상 Architecture
        
        ![image](https://github.com/statrav/Datastructure/assets/109338312/ea27afb3-fb68-492f-8aae-c65960e380cb)
        
        - Backbone : SCGAN architecture
        - Delete Element : y_eyes, y_skin
        - Input Image
            - (기존) Content Image, Style Image (2개)
            - (변형) Content Image (1개)
        - Stylecode Z 단계 후에 CLIP transformer model 추가
            - Style Loss 변형 기대

- 가상 실험
    - 가정 1. 단순 Concept Language Input
        
        ![image](https://github.com/statrav/Datastructure/assets/109338312/eb904ce9-47b8-44cc-9339-3018f19fa88e)
        
    - 가정 2. Input 자연어에 Constrict 두기
        
        ![image](https://github.com/statrav/Datastructure/assets/109338312/b159d134-182c-4f41-8b5f-32f462f7a6fc)
        ![image](https://github.com/statrav/Datastructure/assets/109338312/59f418e6-8653-4232-a456-fce991b4ddf5)
        ![image](https://github.com/statrav/Datastructure/assets/109338312/9c7de5da-0929-41a9-bfe3-726ac46819fe)
        

- Limitation
    - Black Area (Vector값 Zero) Region에 대한 Learning Exclusion 실패
    - Color Code 학습 실패로 인한 상업적 사용의 한계
    - 이미 활성화되어있는 Makeup AI Model로 인한 연구 진행 가치 하락
