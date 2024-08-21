# 함수의 리턴 값은 하나다.

def add_and_mul(a,b):
    return a+b, a*b

print(add_and_mul(3,4)) # 출력해보면
# (7, 12) 이렇게 나온다 
# 하지만 우리가 보기엔 2개 같지만 자세하게 보면 
# 튜플 형태로 나온것을 볼수 있다.
# 결국 튜플 하나로 리턴 된 것이다.

a, b = add_and_mul(4,5) # 그래서 리턴 값을 이렇게 구조분해 할당 시켜서 따로 사용도 가능하다.
print(a)
print(b)

# 하지만 실재로 return 을 2개를 쓰는건 불가능하다
def add1_and_mul1(a,b):
    return a + b
    return a * b
print(add1_and_mul1(7,8)) # 아래 곱하기 return은 무시가 된다.
# 이런식으로 쓰면 안된다.
# return 은 함수를 종료시킨다는 뜻 이므로 종료된 함수는 종료를 또 시킬수 없기 때문이다.

