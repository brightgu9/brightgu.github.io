# 50명의 승객을 태우는데 소요 시간이 5분에서 15분 사이의 손님만 태울 수 있음

from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1~ 50 이라는 수(승객)
    time = randrange(5,51) # 소요 시간 5분~50분
    if 5 <= time <= 15: # 5분에서 15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt +=1 # 증가 처리
    else: # 탑승 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))

print("총 탑승 승객 : {0} 분".format(cnt))