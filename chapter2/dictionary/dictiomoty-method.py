# 딕셔너리 관련 기능들 
# key 리스트 만들기 (keys())
a = {'name':'pey', 'phone':'010-1111-2222', 'birth':'1118'}
print(a.keys()) # 딕셔너리의 key 들을 dict list로 나열해준다.
# dict list 와 list 의 차이는 list 에 비해 메모리를 덜 차지한다고 한다.
print(list(a.keys())) # list 로 형 변환 해주면 리스트로 나열해준다.

# 리스트를 사용하는 이유 예제
# 딕셔너리를 순회하면서 key 를 갖고 오는 예제
for k  in a.keys():
    print(k)


# value 리스트 만들기 (values())
print(a.values()) # 이거 역시 dict values list 로 나열해준다.

# key, value 쌍으로 리스트 만들기 (items())
print(a.items()) # key value 를 튜플 형태로 묶어 리스트로 만들어준다.

# 딕셔너리 비우기 (clear())
a.clear()
print(a) # 키,값이 없는 딕셔너리가 출력되게 된다.

# key 로 value 얻기 (get())
a = {'name':'pey', 'phone':'010-1111-2222', 'birth':'1118'}
print(a['name']) # 원래는 딕셔너리변수명[키명] 으로 value 를 가져온다.
print(a.get('name')) # 딕셔너리변수명.get(키명) 으로 도 value 를 가져온다.
print(a.get('없는 변수')) # 차이로는 없는 변수 명을 넣으면 오류를 내보내지 않고 none 이라고 출력해준다.
print(a.get('없는 변수', '값이 없습니다.')) # 또한 get 메서드는 값이 없을때 출력문을 정해줄수 있다.

# 해당 key가 딕셔너리 안에 있는지 조사하기 (in)
# 사용법 - "찿는키명 in 딕셔너리변수명"
print('name' in a ) # 있으면 true 
print('name' in '없는 변수') # 없으면 false 
# 불리안 형태로 결과값을 출력해준다.

