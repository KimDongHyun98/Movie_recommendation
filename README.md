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
-**데이터 레이어 구조**:
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

### 3. 딥러닝(DL)
-**BERT 기반 장르 임베딩**: 영화 설명 텍스트를 임베딩하여 사용자 관심사와 유사한 영화 추천 

---

## 서비스 구축(Deployment)
- **MLflow Model Registry**
    추천 모델 등록, 버전 관리 및 자동 로드, 서빙, 최종 배포 모델은 BERT 기반 장르 임베딩 모델 사용
    
- **Flask 웹 서비스**
    -**입력**: 사용자가 재밌게 본 영화 목록
    -**출력**: 추천 영화 목록 (TMDB 포스터 이미지 포함)
    -**구현 방식**: 모델 예측 -> 추천 영화 ID 추출 -> TMDB 이미지 연동

---

## 프로젝트 구조(Project Structure)
├── data_preprocessing/ # 원본 및 전처리 노트북
│ ├── bronze_layer.ipynb # 원천 데이터 적재
│ ├── silver_layer.ipynb # 전처리 및 통합
│ └── gold_layer.ipynb # feature 추출 완료
│
├── models/ # 추천 모델 구현
│ ├── recommendation_algorithms/ # ALS, 콘텐츠 기반 등
│ ├── machine_learning/ # SparkXGB 모델
│ └── deep_learning/ # BERT 기반 임베딩
│
├── service/ # 웹 서비스 구현
│ ├── app.py # Flask 메인 서버
│ ├── recommendation_service.py # 추천 로직 처리
│ ├── mlflow_model_load_test.ipynb # 모델 로드 테스트
│ └── templates/ # HTML 템플릿
│
├── config.py # 경로 및 설정 관리
└── README.md

---

## 사용 기술 스택 (Tech Stack)
- **데이터 처리**: PySpark, Unity Catalog  
- **모델링**: ALS, XGBoost, BERT  
- **모델 관리**: MLflow  
- **서비스 배포**: Flask, HTML  
- **인프라**: Azure Databricks

