def sequential_search(A, key):
    for i in range(len(A)):
        if A[i]==key:
            return i
    return -1

l=[5, 3, 8, 4, 2, 7]
print(sequential_search(l, 4))