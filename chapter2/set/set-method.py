# 집합 관련 함수 기능들
# 1개 값 추가하기 add()
s1 = set([1, 2, 3])
s1.add(5)
# s1.add([1,2]) # add 로 추가할때는 1개 씩만 넣어주어야 작동한다.
s1.add("hello") # add 에 문자열을 넣으면 하나로 넣어준다
print(s1)

# 값 여러개 추가하기 update()
s1.update("hello") # update 로 넣으면 문자열을 분해해서 나누어 넣어준다.
s1.update([3, 4, 5, 6])
print(s1)

# 특정 값 제거하기 remove()
s1.remove(3) # remove 메서드 사용시 인덱스가 아닌 실제 값을 넣어주어 삭제할 대상을 지정해준다.
print(s1)
s1.remove("h")
print(s1)
# s1.remove([1, 2, "hello"]) # 한번에 하나씩만 삭제해주어야 한다 여러개 삭제하면 에러를 발생한다.
print(s1)

# 집합을 사용하는 경우
# 리스트로 저장한 중복이 있는 데이터의 값들을 중복 제거하여 사용하고 싶을때 집합을 사용한다.
l1 = [1,1,1, 2,2,2, 3,3,3, 4]
s1 = set(l1)
l1 = list(s1)
print(l1) # 이렇게 사용하면 중복 제거된 리스트값을 갖게 된다.