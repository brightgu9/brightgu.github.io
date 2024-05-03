# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#           .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 22, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업 = 나이, 사용언어 같음

# def profile(name, age = 17, main_lang="파이썬"): # 값이 없는 부분만 할당해주기
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#           .format(name, age, main_lang))
    
# profile("유재석")
# profile("김태호")
# 이름 : 유재석   나이 : 17       주 사용 언어 : 파이썬
# 이름 : 김태호   나이 : 17       주 사용 언어 : 파이썬

# ----------------------------------------------

# 할당

def profile(name, age, main_lang):
    print(name, age, main_lang)

# 순서가 달라도 할당됨.
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", name="김태호", age=23)