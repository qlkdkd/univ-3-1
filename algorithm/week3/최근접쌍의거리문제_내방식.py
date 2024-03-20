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