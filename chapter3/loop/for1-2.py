# for 문 사용 예제

marks = [90, 25, 67, 45, 80] # 학생들의 시험 점수 리스트

number = 0 # 학생에게 붙여 줄 번호
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d 번 학생은 합격 입니다." % number)
    else:
        print("%d 번 학생은 불합격 입니다." % number)