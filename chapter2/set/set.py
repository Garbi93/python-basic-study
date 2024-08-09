# 집합
# 다른 언어에서는 못보던 개념인데 파이썬에서는 
# 자료형으로 제공해준다.
# 집합에 관련한 것을 쉽게 처리하기 위해 만든 자료형이다.

# 집합 만들기
s1 = set([1, 2, 3]) # set 안에 리스트를 만들어 넣는 방식
print(type(s1)) 
print(s1) # 출력해보면 중괄호로 나올텐데 중괄호로 key value 방식으로 나오면 딕셔널, 단순 value 로만 나오면 집합 이라고 한다.
s2 = set("hello") # set 안에 문자열을 넣어 만드는 방식
print(type(s2)) 
print(s2) # 문자열을 집합으로 하면 중복은 제거하고 순서 구분 없이 문자를 하나씩 뜯어서 저장한다.
s3 = {1, 2, 3} # 그냥 중괄호에 key value 구분 없이 value 만 넣어주면 집합으로 만들어진다.
print(type(s3))
print(s3)

# 집합은 인덱스 값이 무작위로 저장 되기 때문에 인덱스를 잡아낼 수 없다.
# 집합은 값이 고유하기 때문에 중복을 허용하지 않는다.

# 집합을 활용하기 위해 리스트로 감싸 인덱스를 고정시켜 사용한다.
l1 = list(s1) # 이렇게 하면 집합에서 리스트로 형변환 되어 인덱싱을 구분하여 사용이 가능해진다.
print(l1) # 리스트 변수로 저장한것을 활용하면 된다.
print(l1[0])

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 교집합 구하기 &
print("교집합: " + str(s1 & s2)) # {4, 5, 6}
# 교집합 함수로 구하기 intersection()
print("함수로 교집합: " + str(s1.intersection(s2)))
print()

# 합집합 | , union
print("합집합: " + str(s1 | s2))
print("함수로 합집합: " + str(s1.union(s2)))
print()

# 차집합 구하기 - , difference()
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))
print()

