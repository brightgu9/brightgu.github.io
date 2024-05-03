# print("python", "java", sep=", ", end="?")
# # python, java
# print("무엇이 더 재밌을까요?")
# python, java?무엇이 더 재밌을까요?
# import sys
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): # 키와 밸류를 튜블로 
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
# 수학      :   0
# 영어      :  50
# 코딩      : 100

# 은행 대기순번표 001, 002, 003....
# for num in range(1, 21):
#     print("대기번호 : "+ str(num).zfill(3)) # 001, 002...

answer = input("아무값이나 입력하세요 : ") # 인풋은 항상 str로 받음
print(type(answer))
print("입력한 값은" + answer + "입니다")

# 아무값이나 입력하세요 : 10
# <class 'str'>
# 입력한 값은10입니다