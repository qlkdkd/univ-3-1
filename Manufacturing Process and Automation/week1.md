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
![image](https://github.com/qlkdkd/school-3-1/assets/71871927/ab653f36-1f83-4d12-83f1-99f71b6f610c)


## 제조 지원 시스템의 기능 분류
* 비즈니스(business function): 고객과 의사소통하는 기능. 판매 및 영업, 주문처리, 수금
* 제품 설계(product design): 연구 및 개발, 설계, 제도, 시제품 제작
* 생산 계획(manufacturing planning): 공정 계획, 생산 계획, 자재소요계획, 능력계획
* 생산 통제(manufacturing control): 제조현장 통제, 재고 관리, 품질 관리


## 생산 시스템의 자동화
### 생산 시스템에서의 컴퓨터 시스템의 활용 목적
* 제조 시스템: 자동화
* 제조 지원 시스템: 정보화 또는 전산화
![image](https://github.com/qlkdkd/school-3-1/assets/71871927/64947ca1-62ab-45fc-8c98-2e75dd335935)

### 제조시스템의 자동화를 위한 컴퓨터 시스템의 종류
* CNC unit
* Robot controller
* Programmable logic controller(PLC)


## 제조시스템의 자동화 장비
* 가공: CNC Machining center, Turning center, Industrial robot
* 조립: Industrial robot
* 운반: AVG(Automated Guided Vehicle), Industrial robot
* 저장: AS/RS(Automatic Storage and Retrieval System)
* 검사: CMM(Coordinate Measuring Machine), Machine vision system


## 제조시스템의 자동화 유형
* 고정 자동화: 가공/조립 작업이 고정됨
* 프로그램가능 자동화: 프로그램에 따라 가공/조립작업이 변경됨
* 유연자동화: 프로그램가능 자동화의 확장. 작업전환 시간이 최소화됨

생산방식|제품/부품|장비|자동화 유형
---|---|---|---
quantity mass production, flow line single model|특정 제품/부품|전용장비 주문제작|고정
job shop production, batch production|다양한 제품/부품|범용장비|프로그램 가능
cellular manufacturing, flow line mixed model|특정 제품군/부품군|전용장비 주문제작|유연

### 제조시스템의 특성과 자동화 유
![image](https://github.com/qlkdkd/school-3-1/assets/71871927/dec8e840-2e6e-43bd-bfc7-6d8a574f57f1)


## 제조 지원 시스템의 전산화
*  ERP(Enterprise Resource Planning): 전사적 자원관리, 기업 내 통합정보시스템
*  CRM(Customer Relationship Management): 고객 관계관리, 마케팅을 위한 고객 정보시스템
*  CAD(Computer Aided Design): 컴퓨터 지원 설계
*  CAM(Computer Aided Manufacturing): 컴퓨터를 이용한 기계 제어 프로그래밍
*  CAE(Computer Aided Engineering): 컴퓨터를 이용한 부품이나 제품의 성능 시뮬레이션
*  CAPP(Computer Aided Process Planning): 컴퓨터 지원 공정 계획
*  MES(Manufacturing Execution System): 제조실행시스템, 제조 현장과 관련한 정보시스템


## 자동화 추진 이유
* 노동 생산성의 향상, 인건비의 절감, 노통력 부족의 해소, 작업의 안전을 제고
* 천편일률적이고 사무적인 업무 또는 3D작업에서 인간을 해방
  * 인간의 기계화를 자동화로 대체
* 수작업으로 불가능한 작업을 수행
* 제품 품질의 향상
* 제조리드타임의 감소


## 자동화 구형 단계
### 자동화의 전제 조건: 안정적이고 충분한 수요
* 자동화는 높은 초기 투자비용 요구-> 이를 회수하기 위해서 수요가 충분해야 함
* 수요의 증가에 따라 점진적으로 자동화를 확대한다.

### 일반적인 자동화 확대 단계
1. 수동 작업장, 수동 자재취급
2. 자동 작업장, 수동 자재취급
3. 자동 작업장, 자동 자재취급

![image](https://github.com/qlkdkd/school-3-1/assets/71871927/342d9c4d-f017-442e-9fe2-655ac320b391)
