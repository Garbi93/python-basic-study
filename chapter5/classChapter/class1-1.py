# 클래스는 반복되는 변수 & 메서드를 미리 정해놓은 틀

# 클래스가 필요한 이유??
# c 언어에는 클래스가 없다 -> 이 말은 굳이 클래스가 없어도 프로그래밍하는데는 문제가 없다.

# 덧셈 계산기를 클래스 없이 만들어 보자

# 누적 더하기 계산기 프로그래밍
result = 0 # 전역 변수 선언 및 초기화

def add(num):
    global result # 전역 변수를 global 로 호출
    result += num  # 전역 변수에 누적 하여 더하기를 해주고
    return result # 전역 변수 result 에 결과값 리턴 하기

print(add(3))
print(add(4))
