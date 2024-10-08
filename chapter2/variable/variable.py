# 변수 개념 정리
# 변수는 어떤 이름을 갖고 있고 값을 담는 상자라고 생각하면된다.
# 변수에 값을 담는개념은 실제로는 변수에 메모리 주소값을 담는다
# 그리고 메모리 주소 안에 실제 값을 저장 한것을 불러온다.
# 이 개념은 자바와 비슷한거 같다.

# 자바나 c 를 배울때는 변수의 자료형 타입을 지정하고 변수 선언후 값을 넣어주었지만
# 파이썬은 변수에 저장된 값을 스스로 판단하여 조금더 편하다.

# 변수가 저장 되는 방식
# 변수 명 = 저장하는 값
# 왼쪽에 있는 정보가 오른쪽으로 덮어 씌워진다.

# 파이썬 주소값 
a = [1, 2, 3] # 리스트를 갖는 변수가 있을때
print(id(a)) # a 의 주소 값을 보면 (id()) 를 사용해 본다. 여기서 신기한 점은 java 의 경우 print(리스트 변수) 를 하면 주소값을 출력하는데 파이썬은 그냥 출력해준다.
# 여기서 이제 a 의 주소를 동일하게 저장하는 b 를 갖게 해보자
b = a 
print(id(b)) # a 와 동일한 주소값을 갖는걸 볼수 있다.
print(a is b) # 동일한 주소값을 갖기때문에 true 가 나온다. 
# 하지만 b 에 a 와 값만 같은 정보를 새로 넣어주면 
b = [1, 2, 3]
print(id(b)) # a 의 주소와 다른 주소를 갖는걸 볼 수 있다.

# 여기서 주소값이 동일한지 확인하는 기능은 is 를 쓴다 
print(a is b) # 지금은 다른 주소값이기 때문에 false 가 나온다.

# 다시 a 와 b 를 동일한 주소로 바라보게 하고 a 의 인덱스 값을 변경하면 b 의 동일한 인덱스에서 어떤 일이 일어나는지 보자
b = a
print(a is b) # 주소가 동일한지 다시 확인 하기 true 가 나온다.
a[0] = 3 # 기존에 0 -> 3으로 변경 
print(a[0]) # 3 이 출력
print(b[0]) # a 주소에 동일한 곳을 찾아가 0번 인덱스의 값을 찾아가면 3 으로 변경된것을 동일하게 출력한다.

# 이렇게 주소자체를 복사하는것이 싫다면 슬라이싱 해서 복사해주면 된다. 아래의 예를 보자
a1 = [1, 2, 3]
b1 = a1[:] # a1의 데이터를 모두 쪼갠것을 b1 에 저장한다. 
# 사실상 새로운 주소를 저장시켜주는것이 아닌 a1 의 값을 기반으로 새로운 값을 생성하여 b1 에 저장해주는 것이기 때문에 깊은복사가 이루어지지 않는다.
print(a1 is b1) # 값 복사만 이루어 지기때문에 false 를 출력 한다.
print(id(a1)) 
print(id(b1))
# 값 복사만 이루어 졌기 때문에 a1 ,b1 의 주소가 다른것을 볼 수 있다.

# 값 복사를 해주는 모듈을 사용하여 값을 복사하기
from copy import copy # 파이썬 모듈 copy를 호출
a2 = [1, 2, 3]
b2 = copy(a2) # 호출한 copy 모듈을 사용 하여 b2 에 a2 값 복사를 해준다.
print(a2 is b2) # 값 복사가 이루어 졌기 때문에 false 가 출력된다.

# 변수의 구조분해 할당 // 튜플 자료형 리터럴 값이 여러 변수가 알맞게 나누어 갖는 것
# 리스트로 해도 동일하게 구조분해 할당이 된다.
a,b = ('python', 'java')
print(a) # 파이썬에서 구조분해 할당이 자동으로 이루어지고 a 에 'pyton' 이 문자열 형태로 저장된다. 
print(type(a)) # 타입을 출력해보면 str 이 출력된다.
print(b)
print(type(b))

# 한변수에 동일한 값을 넣어주고 싶을때
a4 = b4=  "pyton"
print(a4)
print(b4)
print(id(a4))
print(id(b4))
print(a4 is b4) # 이때는 동일한 주소를 가리키게 된다.

# 서로 다른 값을 교체 하고 싶을때 
# 파이썬에서는 임시 변수 지정 없이 바로 변경해주는 기능이 있다.
a6 = 3
b6 = 5
a6,b6 = b6,a6
print(a6)
print(b6) 
# 서로 값을 교체한것을 볼 수 있다.