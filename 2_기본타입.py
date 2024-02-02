# from random import *

# date = randint(4,28)

# print("매월"+ str(date)+"일로")

# jumin = "020108-2234567"

# print("성별 : " + jumin[7])
# print("년 : " + jumin[:2])
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# a = ""
# if jumin[7] == "1":
#     a = "남자"
# elif jumin[7]== "2":
#     a = "여자"

# print(a)
    
# python = "Python is amazing"

# print(python.upper()) # lower()
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "C++"))

# print("나는%d살입니다." % 20) # &s (str), %c (한글자만 받음)
# print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# print("나는 {}살입니다.".format(20))
# print("나는 {1}색과 {0}색을 좋아해요.".format("빨간", "파란"))

# print("나는 {age}살이며, {color} 색을 좋아해요".format(age = 20, color = "빨간"))

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color} 색을 좋아해요")

# \n
# print("백문이 불여일견 \n백견이 불여일타")
# \"
# print("저는 \"나도코딩\"입니다")
# \\ : 문장 내에서  or /
# print("C:\\Users\\admin\\Desktop\\PythonWorkSpace")

# print("Red  apple\rPine") # 뒷 문자를 앞으로 이동(수정)
# print("redd\bapple") # \b 앞글자 하나 삭제
# print("redd\tapple") # tab


# 문제 3
# url = "http://naver.com"
# url = "http://daum.net"
url = "http://google.com"
# print(url[7:])
my_str = url.replace("http://", "")  # (a, b) a 를 b(공백)으로 출력
my_str = my_str[:my_str.index(".")] # 점 나오기 전까지 찾아서 출력
# print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1}입니다.".format(url, password))