def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
if __name__=='__main__':
    n=int(input("숫자 입력: "))
    print("입력한 숫자의 팩토리얼 값: ", factorial(n))