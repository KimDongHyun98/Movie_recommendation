# 사용자 맞춤 영화 추천 시스템 구축 및 웹 서비스 구현

**Azure Databricks 기반 개인화 영화 추천 서비스**

---

## 개요(Overview)

본 프로젝트는 사용자의 영화 시청 기록과 콘텐츠(장르) 정보를 기반으로 **개인화된 영화 추천**을 제공하는 시스템입니다.

**Azure Databricks**환경에서 **Pyspark 기반 추천 모델**을 구현하고,
**MLflow**를 통해 모델을 관리·배포 하며, **Flask**로 웹 서비스를 구축하여 추천 결과를 제공합니다.

-**기간**: 2025.05.26 ~ 2025.06.11

-**목표**: 재밌게 본 영화를 입력하면, 맞춤형 추천 영화 출력

-**특징**: 대용량 데이터 병렬 처리, 다양한 알고리즘 실험, 서비스 구현

---

## 데이터

-**사용 데이터**: Movielens (32M), IMDB, TMDB API

-**데이터 저장 및 관리**: Unity Catalog 사용

-**데이터 레이어 구조**: Medallion Architecture (Delta Lake)

Delta Lake의 Medallion Architecture에 따라 데이터를 계층적으로 처리하여, 신뢰성 있고 재사용 가능한 데이터 파이프라인을 구성하였습니다.

![image](https://github.com/user-attachments/assets/a8165b9e-a520-4678-941e-a9f80c653f16)
출처: [Databricks - Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture)




    -'bronze': 원본 데이터 적재 (MovieLens)    
    -'silver': 데이터 정제 및 통합 (평점수 기반 필터링)
    -'gold': 추천 특성 추출 및 전처리 완료 데이터셋
   
---
   
## 모델

### 1. 추천 알고리즘(Recommender Algorithms)

-**ALS(Alternating Least Squares)**: 사용자-아이템 평점 행렬 기반 협업 필터링


-**콘텐츠 기반 추천**: 장르 정보 -> CountVectorizer -> Cosine Similarty 기반 유사 영화 추천
        

### 2. 머신러닝(ML)

-**SparXGBClassifier (XGBoost)**: 사용자 및 영화 특성을 바탕으로 평점 4점 이상 여부 예측

    -장르 컬럼을 숫자 벡터로 변환하는 파이프라인 구축
    -Optuna 사용해 하이퍼파라미터 최적화
    -SHAP을 이용한 Feature Importance 확인하여 해석력 높임

### 3. 딥러닝(DL)

-**BERT 기반 장르 임베딩**: 영화 설명 텍스트를 임베딩하여 사용자 관심사와 유사한 영화 추천 

    -기존 BERT모델에 장르 정보를 임베딩 벡터로 변환하여 학습
    -영화의 장르 정보를 원-핫 인코딩하여 모델의 입력 데이터로 결합
    -MLM(Masked Language Model) 학습 전략 사용 시퀀스의 일부를 의도적으로 가리고, 모델이 주변 문맥을 통해 가려진 부분을 예측하도록 훈련

---

## 서비스 구축(Deployment)

- **MLflow Model Registry**

    추천 모델 등록, 버전 관리 및 자동 로드, 서빙, 최종 배포 모델은 BERT 기반 장르 임베딩 모델 사용
    
- **Flask 웹 서비스**

    -**입력**: 사용자가 재밌게 본 영화 목록
    ![image](https://github.com/user-attachments/assets/a4ea184a-ce8b-47d5-8238-36ab2e6b3377)
  
    -**출력**: 추천 영화 목록 (TMDB 포스터 이미지 포함)
    ![image](https://github.com/user-attachments/assets/3b344e73-cc74-4474-a323-85bafe677b6b)
  
    -**구현 방식**: 모델 예측 -> 추천 영화 ID 추출 -> TMDB 이미지 연동


---

## 사용 기술 스택 (Tech Stack)
- **데이터 처리**: PySpark, Unity Catalog  
- **모델링**: ALS, XGBoost, BERT  
- **모델 관리**: MLflow  
- **서비스 배포**: Flask, HTML  
- **인프라**: Azure Databricks


