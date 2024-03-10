def unique_elements(A):
    n=len(A)#입력의 크기=리스트의 크기
    for i in range(n-1):#i=0, 1,~, n-2
        for j in range(i+1, n):#j=i+1, i+2, ~, n-1
            if A[i]==A[j]:
                return False
    return True

#알고리즘 테스트
if __name__=='__main__':
    A=[32, 14, 5, 17, 9, 11, 14, 26, 29]
    B=[13, 6, 8, 7, 12, 25]
    print(A, unique_elements(A))
    print(B, unique_elements(B))