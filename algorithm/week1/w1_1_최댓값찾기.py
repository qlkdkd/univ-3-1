def find_max(A):
    max=A[0]
    for i in range(len(A)):
        if A[i]>max:
            max=A[i]
    return max

if __name__=='__main__':
    a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_max(a))