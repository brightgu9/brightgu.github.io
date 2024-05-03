gun = 10

# def checkpoint(soldiers): # 경계 근무
#     global gun # 전역 공간에 있는 gun 변수 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun)) 
# checkpoint(4) 
# print("남은 총 : {0}".format(gun))

# 전체 총 : 10
# [함수 내] 남은 총 : 6
# 남은 총 : 6

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun)) 
gun = checkpoint_ret(gun, 4) 
print("남은 총 : {0}".format(gun))

# 전체 총 : 10
# [함수 내] 남은 총 : 6
# 남은 총 : 6