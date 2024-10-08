# 파이썬의 직관적인 특징을 가장 잘 보여주는 것이 for 문 이다.
# while 문과 비슷한 반복문이고, 
# for 문은 문장 구조가 한눈에 들어온다는 장점이 있다.
# 나는 개인적으로 while 문보다는 for문을 자주 사용했다.

# for 문의 기본 구조
# for 변수 in 리스트 (또는 튜플, 문자열):
#   수행할 문장1
#   수행할 문장2
#   ,,,

# 예)
list1 = ['one', 'two', 'three']
for i in list1:
    print(i)
# java 의 향상된 for 문을 보는거 같다.

# 다양한 for 문의 사용 
a = [(1,2), (3,4), (5,6)] # a 라는 리스트 안에 각각의 튜플이 존재한다.
for (first, last) in a: # 이런식으로 구조 분해 할당을 해 사용 가능하다.
    print(first + last)

for i in a: # 튜플 구조만 뽑아보고 싶어서 한번 사용함
    print(i)
 
# for 문은 어떤 변수의 값을 뽑아와서 비교해가면서 반복하고 싶을때 사용하고
# while 문은 특수한 상황및 조건에 반복하고 싶을때 주로 사용한다.