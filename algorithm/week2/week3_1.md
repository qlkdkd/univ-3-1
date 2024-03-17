# 3. 억지 기법과 완전 탐색
## 억지기법(brute-force)
* 문제의 정의를 바탕으로 한 가장 직접적인 방법
* brute-force method는 naive method라고도 함
* 예: 최대공약수 방법, $a^n$을 구하는 알고리즘 등
$$a^ n=1\times a\times ... \times a$$(시간복잡도: $O(n)$)

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
