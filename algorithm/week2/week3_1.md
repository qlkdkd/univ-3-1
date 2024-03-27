# 3. 억지 기법과 완전 탐색
## 억지기법(brute-force)
* 문제의 정의를 바탕으로 한 가장 직접적인 방법
* brute-force method는 naive method라고도 함
* 예: 최대공약수 방법, $a^n$을 구하는 알고리즘 등
$$a^ n=1\times a\times ... \times a$$

(시간복잡도: $O(n)$)

### 억지 기법의 중요성
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/51f09767-0212-4ad8-9120-20f4540a147b)

## 3.1. 선택 정렬
* 정렬: 레코드들을 키(key)의 순서로 재배열하는 것
### 정렬을 위한 기본 전략
> 입력 리스트에서 가장 작은 항목을 찾고, 이것을 꺼내 정렬된 리스트에 순서대로 저장한다.

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/d335067a-57fa-4c48-8f38-0c20389d0e12)
* 입력 리스트를 오른쪽 리스트라 하고 정렬된 리스트를 왼쪽 리스트라고 하자. 맨 처음에는 모든 숫자가 오른쪽 리스트에 들어 있다.
* 이제 오른쪽 리스트에서 가장 작은 숫자를 선택하여 왼쪽 리스트의 맨 뒤로 이동한다.
* 이 작업을 오른쪽 리스트가 공백상태가 될 때까지 반복한다.

### 제자리 정렬을 위한 알고리즘 개선
* 위 알고리즘은 정렬을 위해 입력 리스트(정렬이 안된 리스트) 외에 추가적인 리스트(정렬된 리스트)를 필요로 함
* 추가적인 저장 공간이 필요하지 않도록 알고리즘을 설계하는 것이 더 좋음.
* **제자리 정렬**: 정렬 알고리즘이 입력 리스트 이외에 추가적인 메모리를 사용하지 않는 방법

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/6d0a221c-fe40-4da7-8632-c57372396267)
* 최솟값 1과 첫 번째 요소 5를 교환하면 전체 배열은 정렬된 부분과 되지 않은 부분으로 나뉨
* 두 번째 요소부터 나머지들 중에서 가장 작은 값을 선택하고 선택된 값을 두 번째 요소(정렬되지 않은 리스트의 첫 번째 요소)와 교환한다.
* 이를 n-1번 반복하면 전체 리스트가 정렬된다.

### 선택 정렬 알고리즘
```python
def selection_sort(A):
    n=len(A)
    for i in range(n-1):
        least=i
        for j in range(i+1, n):
            if (A[j]<A[least]):
                least=j
        A[i], A[least]=A[least], A[j]
        printStep(A, i+1)


def printStep(arr, val):
    print('Step %2d='%val, end='')
    print(arr)

data=[5, 3, 8, 4, 9, 1, 6, 2, 7]
print('Original: ', data)
selection_sort(data)
print('Selection: ', data)
```
* 내부 루프의 최소 항목을 찾는 범위(i+1~n-1)와 리스트의 두 항목을 서로 교환하는 파이썬 코드에 유의

### 복잡도 분석
* 입력의 크기: 리스트의 전체 항목의 수 n
* 기본 연산: 비교 연산(A[j]<A[least]
* 입력구성(찾는 대상의 위치)에 따른 차이: 입력에 상관없이 항상 일정한 횟수의 비교 연산이 필요
    * 즉 선택 정렬은 최선, 최악, 평균 등을 나누어 분석할 필요가 없음
 
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/bfca3999-db00-44f9-9591-04d18c4623b3)

## 3.2. 순차탐색
* 탐색: 주어진 항목들 중에서 "탐색키"라 불리는 원하는 값을 가진 항목을 찾는 것
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/6f792514-f175-49f8-82e6-b73ae8357c4d)
* 순차탐색(선형탐색): 입력리스트의 첫 항목부터 순서대로 하나씩 탐색키와 비교한다
* 순차탐색은 특히 정렬되지 않은 리스트에서도 원하는 항목을 찾을 수 있는 방법

```python
def sequential_search(A, key):
    for i in range(len(A)):
        if A[i]==key:
            return i
    return -1

l=[5, 3, 8, 4, 2, 7]
print(sequential_search(l, 4))
```

### 복잡도 분석
* 최선의 경우: 리스트의 첫 번째 항목이 key인 경우: $T_{best}(n)\in O(1)$
* 최악의 경우: 찾고자 하는 숫자가 리스트에 없거나 맨 뒤에 있는 경우: $T_{worst}(n)=n\in O(n)$
* 평균적인 경우: 리스트의 모든 숫자가 골고루 한번씩 key로 사용되는 경우: $T_{avg}(n)=\frac{n+1}{2}\in O(n)$

## 3.3. 문자열 매칭
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/5698734c-bba7-4b0c-8c41-cae8d38d1767)
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/afb73141-3910-4ef1-9300-61bafe7781ab)
* 패턴의 첫 번째 문자는 'L'인데 텍스트의 첫 번째 문자는 'H'로 서로 다르다.
* 따라서 패턴의 다음 문자 'O'를 비교할 필요도 없이 입력의 다음 문자로 이동한다.
* 이 과정은 패턴의 첫 번째 문자가 일치할 때까지 반복된다.
* 세 번째 위치에서 일치하였으므로, 이제 패턴의 두 번째 문자 'O'를 텍스트와 비교한다.
* 텍스트의 문자 'L'과 다르므로 다시 패턴 전체를 다음 위치로 이동한다.
* 네 번째 위치에서 드디어 패턴의 모든 문자가 일치하였고, 따라서 이 위치를 반환하면 된다.
```python
def string_matching(T, P):#T는 입력, P는 패턴
    n=len(T)
    m=len(P)
    for i in range(n-m+1):
        j=0
        while j<m and P[j]==T[i+j]:#패턴 문자열을 모두 비교
            j=j+1
        if j==m:# 모든 문자가 일치하면, 매칭 성공
            return i#현재 위치 반환
    return -1#문자열 매칭 실패


Str='HELLO WORLD'
print(string_matching(Str, 'LO'))
```

### 복잡도 분석
* 입력의 크기: 텍스트의 길이 n과 m
* 기본 연산: 6행 (P[j]==T\[i+j\])

* 최선의 경우: 텍스트 T의 맨 앞의 문자열이 패턴 P와 일치하는 경우. 패턴의 길이인 m번의 비교만으로 문자열 매칭이 종료됨
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/afb8a460-d592-429a-b309-132bdd507d15)
* 최악의 경우: 각 위치에서도 패턴의 모든 문자를 비교해야 하는 경우
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/99b30487-c9d0-45f4-8a6f-9b26cb7676cd)

## 3.4. 최근접 쌍의 거리
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/28eda51f-bc87-49d3-8068-daf3565336b9)

### 억지 기법의 최근접 쌍의 거리 전략
거리 계산: 유클리드 거리 사용

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/e8b8f1f4-8093-4b7d-b296-5c4d32695b98)
```python
import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]+p2[1])**2)

def closest_pair(p):
    n=len(p)
    min_dist=float("inf")
    for i in range(n):
        for j in range(i+1, n):
            dist=distance(p[i], p[j])
            if dist<min_dist:
                min_dist=dist
    return dist

p=[(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("최근접 거리: ", closest_pair(p))
```
[비교: 내가 짠 방식](![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/15487275-0ba7-4875-b168-28ef0bad6718)
)
```python
import math # math 모듈 포함. 제곱근(sqrt) 함수 사용을 위해
def distance(p1, p2): # Euclidean 거리 계산 함수
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
def closest_pair(p):
    n=len(p)
    d=[]
    for i in range(n-1):
        for j in range(i+1, n):
            d.append(distance(p[i], p[j]))
            
    d.sort()
    return d[0]
                
p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("최근접 거리:", closest_pair(p))
```

### 복잡도 분석
* 입력의 크기: n
* 기본 연산: `dist=distance(p[i], p[j])`
* 효율: 입력의 구성과는 관련이 없어 최선, 평균, 최악의 경우에 대해 항상 동일함

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/c5a330f3-260d-4cac-8101-4e033bc81067)
