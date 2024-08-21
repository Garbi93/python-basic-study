# for 문과 countinue 문
# while 문에서 했던거와 비슷하게 countinue 문을 사용해서 
# 특정 조건에서 이하 동작을 무시하고 다시 처음으로 되돌리는 기능 


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60: # 60 점 미만의 점수라면 불합격 이므로 
        continue # print 출력 못시키게 하기
    print("%d번 학생 축하합니다. 합격 입니다." % number) 