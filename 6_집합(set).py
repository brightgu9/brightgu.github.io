# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}

# print(my_set) # {1,2,3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#  교집합 ( java 와 python을 모두 할 수 있는 사람)

# print(java & python) # {'유재석'}
# print(java.intersection(python)) 위 코드랑 동일

# 합집합
# print(java | python)
# print(java.union(python)) # 순서는 실행시킬때마다 바뀜

# 차집합 ( java 할 수 있지만, python 은 할 줄 모르는 개발자)
# print(java-python) # 양세형, 김태호
# print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호") # set 에 추가
# print(python)
java.remove("김태호")
# print(java) # 유재석, 양세형