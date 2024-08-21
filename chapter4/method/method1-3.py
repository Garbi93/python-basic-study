# return 을 활용하기
# 함수를 빠저나가고 싶을때 사용하기도 한다,

def say_nick(nick):
    if nick == "바보":
        return # nick 변수가 바보 라면 함수를 종료
    print("나의 별명은 %s 입니다." % nick) # 아니면 그냥 print 하는데 nick 변수안에 들어있는것을 사용하여 출력
say_nick("갈비")
say_nick("바보") # return 하여 아무것도 실행되지 않고 종료 된것을 볼 수 있다.
say_nick("만두") 