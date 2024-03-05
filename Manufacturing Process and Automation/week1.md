# 생산 시스템과 자동화 개요
## 생산 시스템
### 생산 시스템의 정의
기업 또는 조직의 제조공정을 성공적으로 수행하기 위해 구성된 사람, 장비, 절차 및 방법의 집합

### 생산 시스템의 구성
#### 제조(manufacturing) 시스템
* 공장, 기계, Blue color
* 자재 처리(material processing)
#### 제조 지원(manufacturing support) 시스템
* 사무실, 컴퓨터, white color
* 정보처리(information processing)
![image](https://github.com/qlkdkd/school-3-1/assets/71871927/6dfc81d6-4e86-4c5b-b498-a395bd58bb37)


## 제조 시스템
### 제조시스템의 구성요소
* 설비
  * 공장건물, 기계, 공구, 장비, 컴퓨터시스템
  * 가공, 조립, 운반, 저장, 검사, 제어를 위한 HW
  
### 제조시스템의 분류
* 이산형(descrete) 제조시스템
  * 부품이나 제품 수량이 자연수
  * 자동차, 반도체, 가전제품
* 연속형(continuous) 제조시스템
  * 부품이나 제품 수량이 실수
  * 화학제품, 식품
![image](https://github.com/qlkdkd/school-3-1/assets/71871927/22f9917f-dc01-418a-85ec-b2ca4d3d8541)

### 기계화와 자동화
* 기계화: 인간이나 동물의 근력을 기계로 대체하는 것
* 자동화: 기계의 제어를 인간 대신 컴퓨터로 대체하는 것

### 제조공정의 분류
* 수작업 공정: 작업자가 동력기계를 제어
* 기계화
  * 작업자-기계 공정: 작업자가 동력기계를 제어
  * 자동화
    * 반자동 공정: 컴퓨터가 동력기계를 제어하고, 작업자는 장착 및 탈착 작업을 수행
    * 완전자동 공정: 컴퓨터가 동력기계와 장탈착 기계를 제어하고, 작업자는 간헐적인 점검이나 운반 또는 주기적인 유지보수 작업을 수행

   
## 제조시스템의 특성
### 생산량
* 소량: 1~100pc/yr
* 중량: 100~10000pc/yr
* 대량: 10000~1000000pc/yr

### 제품다양성(product variety)
* 제품 유형 수: 소품종, 중품종, 다품종

### 생산량과 제품 유형 수에 따른 제조시스템의 분류
* 생산량과 제품 유형 수 간에는 역 상관관계가 존재
  * 기술 발전으로 다품종 대량생산의 비중이 점차 증가하는 추세
![image](https://github.com/qlkdkd/school-3-1/assets/71871927/8041c808-75a8-4c92-8b98-ce869266bc59)

### 제품 다양성
#### 제품 간 다양성
* 경 다양성(hard variety)
  * 공통된 부품 또는 공정의 비율이 낮다
  * 제품 범주가 다르다.(예: 자동차와 트럭)
* 연 다양성(soft variety)
  * 공통된 부품 또는 공정의 비율이 높다
  * 제품 범주는 같고, 모델이 다르다.(예: 배기량과 선택사양이 다른 승용차)
  * 
### 제품 복잡성
#### 부품: 공정 수
* 예: 플라스틱 사출 성형 부품의 공정 수는 1, IC칩의 공정 수는 75
#### 조립품: 부품 수
* 예: 샤프펜슬의 부품 수는 10, 항공기의 부품 수는 1,000,000, 우주왕복선의 부품 수는 10,000,000

### 배치 유형
* 고정위치 배치(fixed-point layout): 가공품이 일정 위치에 고정. 대형 제품의 조립
* 공정별 배치(process layout): 장비의 기능별로 배치
* 셀 배치(cell layout): 유사 제품/부품 그룹별로 장비 배치
* 제품별 배치(product layout): 제품별로 다수의 작업장을 순차적으로 배치
![image](https://github.com/qlkdkd/school-3-1/assets/71871927/7f6b2870-1a0b-449f-9e6c-aa4a30ef0a59)
![image](https://github.com/qlkdkd/school-3-1/assets/71871927/2d386379-7f2b-4a23-a01c-badcdbc69d42)

### 제조시스템의 생산 방식
* job shop production: 주문생산
* batch production: batch 단위생산, setup time이 길다
* cellular manufacturing: 유사 부품 그룹별 생산, setup time이 짧다
* quantity production: 단일 장비에서 단일 부품을 대량 생산
* flou line production
  * single model: 한 가지 제품만을 생산
  * mixed model: 유사한 제품/부품 그룹을 동시 생산

### 연간 생산량, 제품 유형수, 제품간 다양성, 제품복잡성에 따른 설비배치와 생산방식
연간 생산량|제품 유형수|제품간 다양성|제품 복잡성|생산 방식|설비배치
---|---|---|---|---|---
소량|다품종|경다양성|-|job shop production|고정배치, 공정별 배치
중량|중품종|경다양성|-|batch production|공정별 배치
중량|중품종|연다양성|-|cellular manufacturing|셀 배치
대량|소품종|-|단일 공정|quantity production|공정별 배치
대량|소품종|-|복수 공정|flow line single model|제품별 배치
대량|소품종|연다양성|복수 공정|flow line mixed model|제품별 배치
