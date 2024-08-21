# 리스트 컴프리 헨션 사용하기
# 패션 코드라서 꼭 알 필요까진

# 예제
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)
# 다음과 같이 빈 배열에 3배를 하여 값을 넣어줄때
# 컴프리헨션을 사용 하면 
a1 = [1,2,3,4]
result1 = [num1 * 3 for num1 in a1]
print(result1)
# 다음과 같이 줄여 쓸 수 있는데 
# 익숙해지면 사용해보도록 하자

# 조건문도 같이 사용 가능하다
a2 = [3,4,5,6]
result2 = [num2 * 3 for num2 in a2 if num2 % 2 == 0] # 짝수일 때만 3을 곱해서 새로운 리스트에 넣어라 
print(result2)
# 이렇게 줄여 쓰고 싶을때도 사용 가능하다.

# for 문 2개를 합쳐서 사용 가능하다
list1 = [x*y for x in range(2, 10) for y in range(1,10)] # 이런식으로 사용도 가능하다.
print(list1)