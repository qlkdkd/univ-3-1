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
