# import travel.thailand
# # import travel.thailand.ThailandPackage # import에서 바로 가져오면 오류

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # 이렇게 from 으로 사용 가능
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# from random import *
from travel import *

# trip_to = vietnam.VietnamPackage()  # 오류 이유
# travel 패키지에 모든 걸 가져오지만, 개발자가 공개를 해야 함
# __init__ 에서 __all__을 써야됨
trip_to = thailand.ThailandPackage()
trip_to.detail()


# docstring 오류 수정해야함
# ->linting 해결
