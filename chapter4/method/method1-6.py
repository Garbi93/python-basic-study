# lambda 예약어
# 패션코드

# 원래 코드는 이런식 이라면
def add1(a,b):
    return a+b

# 람다식으로 표현하면
add2 = lambda a, b: a+b

result1 = add1(3,4)
result2 = add2(3,4)

print(result1)
print(result2)
# 이런식으로 줄여서 표현도 가능하다.

# 람다 함수를 활용하는 이유??
# 람다 함수같은 경우 함수명을 쓸 필요 없다
# 그래서 리스트 내부에 바로 사용이 가능하다 
# 람다 함수 예)
a = [lambda a, b: a+b, lambda a, b: a*b] # 어떤 하나의 변수 안에 람다로 여러 기능들을 담았다.
print(a[0](5,7)) # 이런식으로 a 변수 안에 0 번 인덱스인 람다식을 호출하면서 바로 사용이 가능하다.
print(a[1](5,7)) # a 의 1 번째를 불러 바로 사용도 가능하다.