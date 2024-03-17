import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]+p2[1])**2)

def closest_pair(p):
    n=len(p)
    min_dist=float("inf")
    for i in range(n):
        for j in range(i+1, n):
            dist=distance(p[i], p[j])
            if dist<min_dist:
                min_dist=dist
    return dist

p=[(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("최근접 거리: ", closest_pair(p))