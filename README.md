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
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/13a365f2-89da-4c3a-be38-71b2f46d63a6/Untitled.png)
        
        - Backbone : SCGAN architecture
        - Delete Element : y_eyes, y_skin
        - Input Image
            - (기존) Content Image, Style Image (2개)
            - (변형) Content Image (1개)
        - Stylecode Z 단계 후에 CLIP transformer model 추가
            - Style Loss 변형 기대

- 가상 실험
    - 가정 1. 단순 Concept Language Input
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fadda56a-b45a-46e2-a7b4-ade58af2715a/Untitled.png)
        
    - 가정 2. Input 자연어에 Constrict 두기
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0f196029-8cd8-421e-bc15-069a8d3df5a5/Untitled.png)
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8be11654-718f-4cee-a9c8-9cf74d20bd4a/Untitled.png)
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c801ba5d-7c20-4d6e-841f-8d9369107b99/Untitled.png)
        

- Limitation
    - Black Area (Vector값 Zero) Region에 대한 Learning Exclusion 실패
    - Color Code 학습 실패로 인한 상업적 사용의 한계
    - 이미 활성화되어있는 Makeup AI Model로 인한 연구 진행 가치 하락
