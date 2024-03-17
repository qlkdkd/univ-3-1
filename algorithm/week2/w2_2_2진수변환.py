def binary_digits(n):#입력: 양의 정수 n
    if n<=1:#n이 1 이하이면 길이는 1
        return 1
    else:#n이 1보다 크면 1+n//2의 길이
        return 1+binary_digits(n//2)
    
n=int(input("변환할 숫자 입력: "))
print(binary_digits(n))