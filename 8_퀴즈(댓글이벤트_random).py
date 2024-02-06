'''
댓글 이벤트
추첨을 통해 1명은 치킨, 3명은 커피 쿠폰
조건1 : 편의상 댓글은 20명이 작성, 아이디는 1~20으로 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈과 shuffle, sample 활용

출력 예제
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
-- 축하합니다 --
'''

from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(lst) # 값을 섞어줌
# print(sample(lst,4)) # 렌덤으로 숫자를 출력 (, 출력할 갯수)

users = range(1,21) # 1~20 까지 숫자 생성
# print(type(users)) # range 타입으로 생성 -> 리스트 요소를 사용할 수 없음
users = list(users) # 리스트로 변환
shuffle(users)
# print(users)

winners = sample(users, 4)
print('-- 당첨자 발표 --')
# print('치킨 당첨자 : {0}'.format(winners[0]))
# print('커피 당첨자 : {0}'.format(winners[1:]))
print('치킨 당첨자 : {0}\n커피 당첨자 : {1}'.format(winners[0], winners[1:]))
print('-- 축하합니다 --')