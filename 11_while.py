# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer,index))
#     index -= 1
#     if index ==0:
#         print("커피가 폐기처분되었습니다")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}남았어요.".format(customer, index))
#     index +=1
#     # 무한루프

# customer = "토르"
customer = input("커피의 주인 : ")
person = "Unknown"

while person != customer:
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
    if person == customer:
        print("네 {0}님 커피 나왔습니다".format(customer))