# height = 0
# gender = ""
def std_weight(height, gender): # 키 m 단위(실수), 성별 남자 or 여자
    # global height, gender
    if gender == "남자":
        return height*height*22
    else:
        return height*height*21

height = 175 # 단위 : cm
gender = "남자"
weight = std_weight(height / 100, gender) # 키 단위 cm -> m
weight = round(weight, 2) # 소수점 둘째자리까지 출력 (셋째자리에서 올림)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다"\
      .format(height, gender, weight))