#  딕셔너리 dictionary
cabinet = {3:"유재석", 100:"김태호"}

# print(cabinet[3]) # 유재석
# print(cabinet[100]) # 김태호

# print(cabinet.get(3)) # 유재석
# print(cabinet[5]) #  값이 없으면 오류
# print(cabinet.get(5)) # 값이 없으면 None

# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
cabinet["A-3"] = "김종국" # value값을 수정
cabinet["c-20"] = "조세호" # value 추가
# print(cabinet)

del cabinet["A-3"] # 키값 삭제
# print(cabinet)

# print(cabinet.keys()) # 키값 출력
# print(cabinet.values()) # value 값 출력

print(cabinet.items()) # 키+밸류 출력
cabinet.clear() # 모든 값 삭제
print(cabinet) # {}