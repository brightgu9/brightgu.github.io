# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end="공백 ") # end 두줄의 프린트문을 한줄로 병합
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language): # 가변인자
    print("이름: {0}\t나이: {1}\t".format(name, age), end="공백 ") # end 두줄의 프린트문을 한줄로 병합
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "C", "C++", "C#", "자바스크립트")
profile("김태호", 25, "Kotlin", "Swift")