# 매개변수에 초깃값 미리 설정하기

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d 살 입니다." % old)
    if man:
        print("남자 입니다.")
    else:
        print("여자 입니다.")
# name, old 매개 변수는 변수만 설정 한것 이고
# man은 아무것도 안들어오면 초기 값으로 무조건 man 이 들어가게 만들어 줬다.
say_myself("홍길동",20) # 이런식으로 man 영역에 아무 값을 안 줘도 남자 입니다를 출력해 준다.
say_myself("황진이",25, False)
# 초기 값이 지정된 변수는 제일 뒤에 써주어야한다는 법칙이 있다.
