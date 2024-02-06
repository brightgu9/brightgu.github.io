absent = [2,5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11): # 1부터 10번까지 출석번호
    if student in absent:
        print("{0}번이 결석했구나".format(student))
        continue
    elif student in no_book:
        print("{0}번아 책이 없어? 오늘 수업 여기까찌, {0}번은 교무실로 따라와".format(student))
        break
    print("{0}번아, 책을 읽어봐".format(student))
    print("{0}번 : 네 선생님".format(student))