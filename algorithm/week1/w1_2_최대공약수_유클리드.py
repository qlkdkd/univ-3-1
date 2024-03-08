def gcd(a, b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

a, b=map(int, input("두 숫자 입력: ").split())
print(f"{a}와 {b}의 최대공약수: {gcd(a, b)}")