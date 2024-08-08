# 2-1 숫자형 데이터
# 정수형 데이터 
# 0을 포함한 소수가 아닌 음수 양수 

a = 123
print(type(a))
# <class 'int'> 라고 타입을 출력 하게 된다. 정수형 데이터를 나타낸다.

b = 1.2
print(type(b))
# <class 'float'> 라고 타입을 출력하게 되고 실수영 데이터를 나타낸다.

c = 0o10
print(c)
print(type(c))
# 8 진수도 정수형이구만??


# 사칙연산
a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
# 나눗셈 하면 원래는 자바에서는 목이 나왔는데 파이썬에서는 값이 나와주네??
# a 의 b 제곱을 나타내는 연산자는 ** 곱하기 연산자를 두번 쓴다
print(a ** b)
print(a % b)
# 파이썬에서 목 값은 // 슬래시 두개로 써서 나타낸다.
print(a // b)

