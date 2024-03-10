def binary_digits(n):
    count=1
    while n>1:
        count=count+1
        n=n//2
    return count

if __name__=="__main__":
    n=int(input('숫자 입력: '))
    print('비트 수: ',binary_digits(n))