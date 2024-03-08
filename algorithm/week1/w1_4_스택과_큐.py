import queue#파이썬 큐 모듈 포함

Q=queue.Queue(maxsize=20)#큐 객체 생성(최대 크기 20)
S=queue.LifoQueue(maxsize=20)#스택 객체 생성(최대 크기 20)

Q.put(20)#큐에 20 삽입(enqueue)
print(Q)

val=Q.get()#큐에서 항목 삭제(dequeue)
print(val, Q)

S.put(20)#스택에 20 삽입(push)
print(S)

val2=S.put(20)#스택에서 항목 삭제(pop)
print(val2, S)