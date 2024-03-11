# 2. 알고리즘 효율성 분석
* 시간 효율성: 더 빨리 결과를 내는 알고리즘이 더 효율적
* 공간 효율성: 알고리즘이 컴퓨터 메모리를 얼마나 사용하는지를 나타냄.
* 둘 중에서 하나를 골라야 한다면 보통은 시간 효율성을 선택함

## 2.1. 효율성 분석의 기초
### 실제 실행 시간 측정 방법
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/772de859-99c9-4101-ae15-38652338827e)
* 실행 시간 측정 방법의 문제점
  * 알고리즘 반드시 구현해야 함
  * 반드시 같은 조건의 하드웨어를 사용하여 실행시간을 측정해야 함
  * 프로그래밍 언어나 운영체제와 같은 소프트웨어 환경도 같아야 함
  * 성능 비교에 사용했던 데이터가 아닌 다른 데이터에 대해서는 다른 결과가 나올 수 있어 실험되지 않은 입력에 대해서는 실행시간을 주장할 수 없음

* 알고리즘의 효율성 평가를 위해 절대적인 시간 측정이 아니라 이론적으로 알고리즘의 복잡도를 분석하는 방법이 주로 사용됨

### 알고리즘 복잡도 분석에서 중요한 점
* 입력의 크기
* 기본 연산
* 어떤 형태로 증가하는가
* 입력의 특성에 따른 알고리즘의 효율성
### 입력의 크기
  * 알고리즘의 효율성은 보통 입력의 크기의 함수로 표현됨
  * 무엇이 입력의 크기를 나타내는지를 먼저 명확히 결정
    * 예1: 리스트 A에서 어떤 값(key)를 가진 항목을 찾는 탐색 문제에서 입력의 크기: `len(A)`
    * 예2: x의 n제곱 값인 $x^n$을 구하는 거듭제곱 알고리즘의 입력의 크기: n
      * x가 크다고 처리시간이 늘어나진 않음
    * 예3: 다항식의 연산: 다항식의 최대차수 b
    * 예4: 가로가 W, 세로가 H인 행렬 알고리즘: W, H
    * 예5: 그래프 연산: V, E
   
### 기본 연산
  * 알고리즘에서 가장 많이 실행되는 연산, 즉 기본 연산을 찾고, 이 연산이 실행되는 횟수만을 계산하는 것
  * 다중 루프의 경우 가장 안쪽 루프에 있는 연산이 가장 많이 실행

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/f5017592-21cd-4870-bffb-5bb72e1dcc72)
  * 알고리즘 A: 곱셈(\*)과 대입(<-)연산이 각각 한 번씩 사용됨-> 총 2회의 계산
  * 알고리즘 B:
    * 반복문 내부의 문장인 3행은 덧셈과 대입 연산이 각각 한번씩 필요
    * 2행에 의해 n번 반복됨->(대입 n번, 덧셈 n번)
    * sum을 초기화하는 문장에서도 한 번의 대입 필요
    * 총 2n+1번의 계산
  * 알고리즘 C:
    * 덧셈 연산: $n^2$번
    * 대입 연산: $n^2+n+2$,번
    * 총 $2n^2+n+2$번
   
### 복잡도 함수와 증가 속도
  * 시간 복잡도 함수: 연산의 수를 n의 함수로 나타낸 것
  * 위 알고리즘의 시간복잡도 함수를 각각 $T_A(n)$, $T_B(N)$, $T_C(N)$이라고 나타내면
$$T_A(n)=2, T_B(n)=2n, T_C(n)=2n^2$$
  * 알고리즘의 효율성 분석은 충분히 큰($n>=n_0)$ 입력에 대해서만 관심이 있음

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/7c77bdb0-c1fd-4983-944e-47eed8e6ad70)
  * 여러 알고리즘이 있을 때 이들을 구현하지 않고도 효율성을 비교하는것은 이와 같이 복잡도 분석으로 가능하다. 특히 이러한 분석은 충분히 큰 입력에 대해, n의 증가에 따른 실행시간의 증가 속도에만 관심이 있다.

### 최선, 최악, 평균적인 효율성
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/3d5accc0-4c1b-4ebe-84f6-5ba95c88c903)

### 예: 순차탐색
```python
def sequentialSearch(A, key):
    for i in range(len(A)):
        if A[i]==key:
            return i
    return -1
        
if __name__=="__main__":
    A=[32, 13, 5, 17, 23, 9, 11, 4, 26, 29]
    print(sequentialSearch(A, 32))#최선의 경우
    print(sequentialSearch(A, 29))#최악의 경우
```
* 최선의 경우: 리스트 A의 첫 번째 항목이 key와 같은 경우
  * $T(n)=1$

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/2029caae-1c35-4826-b180-ad21175ce23a)

* 최악의 경우: 탐색키 key가 리스트에 없거나 맨 뒤에 있는 경우
  * $T(n)=n$
 
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/4f9919c7-0aee-4936-8970-b4e0e269e4f6)

* 평균: 가정이 필요
  * 비교 연산의 횟수를 모두 더한 다음, 이것을 전체 숫자의 개수로 나누어주면 평균적인 경우의 비교 연산의 수행 횟수를 알 수 있음

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/c5ba168b-56b6-433c-ad43-2158749a75ee)

## 2.2. 점근적 성능 분석 방법
* 복잡도 함수에서 차수가 가장 큰 항이 절대적인 영향

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/105e06ab-19b4-404c-800b-ab897d662227)

### 점근적 표기
* n이 무한대로 커질 때의 복잡도를 간단히 표기하기 위해 사용
  * 복잡도 함수의 최고차항을 계수 없이 취해 단순화함
* 빅오 표기법, 빅오메가 표기법, 빅세타 표기법

### 빅오 표기법
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/5d6370f7-173a-42c5-9e46-c6f8325100a5)
### 빅오메가 표기법
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/6864d868-2851-4f0a-b764-0d24109400fe)
### 빅세타 표기법
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/3ba322bc-222e-4b4e-b7ed-93a7aa4964e4)
### 다단계 알고리즘의 복잡도
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/253296ca-c9f5-4f10-b419-7484628f796b)
* 예: 리스트의 중복 항목 검사

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/13edbaac-65a2-40f9-aa88-91f816d57ee0)
  * 알고리즘 A: 리스트의 각 항목을 다른 모든 항목과 비교하여 같은 항목이 있으면 True, 없으면 False를 반환. 이중 루프로 구현
  * 알고리즘 B: 2단계 알고리즘 사용

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/efffd181-f38a-41e8-b894-0f873353cace)

    * 1. 리스트를 항목 크기순으로 정렬
    * 2. 정렬된 리스트에서 인접 항목을 비교하여 같은 항목이 있으면 True, 없으면 False 반환

* 복잡도 계산
  * 1단계 정렬: $O(nlog_2n)$
  * 2단계: for loop 하나만 사용-> 인접 항목만 비교-> $O(n)$
  * 전체: $O(max{nlog_2(n), n})=O(nlog_2(n))
 
### 점근적 성능 클래스들
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/e2ec0b41-70fd-4f7d-b98e-566e3d337d80)
* 상수형($O(1)$): n이 변하더라도 항상 일정한 시간에 처리됨
* 로그형($O(log(n))$): 알고리즘이 반복될 때마다 문제의 크기가 상수배만큼 작아지는 매우 효율적인 방법. 이진탐색
* 선형시간($O(n)$): n에 비례하는 시간이 걸리는 것
* $O(n*log(n))$: 많은 분할정복기법 알고리즘에서 흔히 나타남. 병합정렬, 평균적인 경우의 퀵 정렬
* $O(n^2)$: 이중루프로 처리되는 알고리즘에 흔히 나타남. 단순한 정렬 알고리즘, $n\mul n$ 행렬 덧셈 뺄셈 등
* $O(n^3)$: 삼중루프로 처리되는 알고리즘. Floyd의 최단경로 알고리즘
* $O(2^n)$: 지수형. 원소의 개수가 n인 집합의 모든 부분 집합을 찾는 문제 등
* 팩토리얼형($O(n!)$): 입력이 수십만개만 되더라도 강력한 슈퍼컴퓨터로도 지구가 탄생하여 지금까지 흘러온 시간보다 더 많은 실행시간이 요구됨

## 2.3. 복잡도 분석 예: 반복 알고리즘
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/e3614234-86cb-4d76-891d-626634945588)
### 자연수의 제곱 계산
```python
#알고리즘 A
def compute_square_A(n):
    return n*n

#알고리즘 B
def compute_square_B(n):
    sum=0
    for i in range(n):
        sum=sum+n
    return sum

#알고리즘 C
def compute_square_C(n):
    sum=0
    for i in range(n):
        for j in range(n):
            sum=sum+1
    return sum
```
* 알고리즘 A: $T(n)=1$, $O(1)$
* 알고리즘 B: $T(n)=n\in O(n)$
* 알고리즘 C: $T(n)=n^2\in O(n^2)$

### 리스트의 중복 항목 탐색
```python
def unique_elements(A):
    n=len(A)#입력의 크기=리스트의 크기
    for i in range(n-1):#i=0, 1,~, n-2
        for j in range(i+1, n):#j=i+1, i+2, ~, n-1
            if A[i]==A[j]:#기본 연산
                return False#같은 항목이 있으면 False 반환
    return True#같은 항목이 없으면 True 반환

#알고리즘 테스트
if __name__=='__main__':
    A=[32, 14, 5, 17, 9, 11, 14, 26, 29]
    B=[13, 6, 8, 7, 12, 25]
    print(A, unique_elements(A))
    print(B, unique_elements(B))
```
* 입력의 크기: 리스트의 전체 항목 수
* 기본 연산: 이중 루프 안에 가장 안쪽에 위치한 5행의 비교연산자 `A[i]==A[j]`
* 최악의 경우: n(n-1)/2번의 비교 필요->$O(n^2)$에 속함
* -> 만약 이 문제를 두 단계 알고리즘으로 해결하면 복잡도를 $O(nlog_2(n))$으로 줄일 수 있음

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/3f7d507d-d2e3-4aa6-bb23-1819081eec7b)

### 자연수의 2진수 변환시 비트 수
```python
def binary_digits(n):
    count=1
    while n>1:
        count=count+1
        n=n//2
    return count

if __name__=="__main__":
    n=int(input('숫자 입력: '))
    print('비트 수: ',binary_digits(n))
```
* 입력의 크기: n
* 기본 연산: 3행의 while문 내부의 문장들이 가장 많이 반복될 것으로 예상할 수 있는데, 4행과 5행이 같은 횟수만큼 반복됨
* n을 $2^k$라고 가정하고 루프가 반복될 때마다 n이 다음과 같이 절반씩 줄어듬

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/98af5462-6623-4e77-80b8-ecd1b5825d2e)
* $n=2^k$->
$$복잡도=O(log_2(n))$$

## 2.4. 복잡도 분석 예: 순환 알고리즘
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/9d5c4921-f38b-4201-b1be-6ae3deaa3de6)
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/665193bc-94b0-427b-a5ad-e1eedcb8eed4)

```python
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
if __name__=='__main__':
    n=int(input("숫자 입력: "))
    print("입력한 숫자의 팩토리얼 값: ", factorial(n))
```
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/542c4564-1fbb-4100-aeec-d6d481ec670d)
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/96b17dbd-deab-446f-b2d0-bbc9bf789515)
