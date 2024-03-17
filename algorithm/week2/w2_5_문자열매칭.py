def string_matching(T, P):#T는 입력, P는 패턴
    n=len(T)
    m=len(P)
    for i in range(n-m+1):
        j=0
        while j<m and P[j]==T[i+j]:#패턴 문자열을 모두 비교
            j=j+1
        if j==m:# 모든 문자가 일치하면, 매칭 성공
            return i#현재 위치 반환
    return -1#문자열 매칭 실패


Str='HELLO WORLD'
print(string_matching(Str, 'LO'))