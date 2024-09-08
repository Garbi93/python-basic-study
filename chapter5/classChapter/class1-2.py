# 만일 한 프로그램에서 2대의 계산기가 필요한 상황이라면???
# 각각 계산기의 결과 값을 저장하기 위해서 
# 다른 전역 변수를 선언해 주어야 한다.

# 계산기 2
result1 = 0
result2 = 1

def add1(num): # 계산기1
    global result1
    result1 += num
    return result1

def add2(num): # 계산기2
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4)) # 1번 끼리 계산
print(add2(3))
print(add2(7)) # 2번 끼리 계산 

# 이런식으로 하면 같은 함수인데 여러개를 만들고 변수도 여러개를 선언해야하는 불편함이 생기게 된다.
# 그래서 class 를 사용하게 된다.