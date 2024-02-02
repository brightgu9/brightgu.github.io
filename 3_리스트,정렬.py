# 리스트 []
'''
subway = ["유재석", "조세호", "박명수"]
# print(subway.index("조세호")) = 1
subway.append("하하")
# print(subway) + 하하

subway.insert(1, "정형돈")
# print(subway) 1번째에 추가

# subway.pop()
print("삭제 : ", subway.pop(), subway)
# print(subway) # 맨 뒤에 요소 삭제

# 같은 이름이 몇 명(몇 개) 있는지

subway.append("유재석")
# print(subway.count("유재석")) # 몇번 나오는지 카운트(int)
'''

# 정렬

num_list = [5,2,4,3,1]
num_list.sort() # 오름차순으로 정렬
# print(num_list) [1,2,3,4,5]

num_list.reverse() # 내림차순으로 정력
# print(num_list) [5,4,3,2,1]

# num_list.clear() 요소 모두 삭제
# print(num_list) []

mix_list = ["조세호", 20, True]
# print(mix_list)

# num_list.extend(mix_list)  # 리스트 확장 a 뒤에 b
print(num_list)