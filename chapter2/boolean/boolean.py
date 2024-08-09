# 불리안 자료형 
# true or false 
# 주로 활용 되는곳은 조건문, 반복문 안에서 조건식으로 사용된다.
a = True # 불리안 자료형은 리터럴 값의 첫 글자를 대문자로 사용한다.
print(type(a))
print(a)
b  = False
print(type(b))
print(b)
a = 1 == 1 # 비교문으로 true false 를 출력할수 있다.
print(a)
a = 1 == 2
print(a)

a = 1 > 2 # 이것 역시
print(a)
a = 1 < 2 
print(a)

# 자료형의 기본 참과 거짓 
# 문자열 자료형
a = "puyton" # 문자열 자료형은 값이 있으면 true
print(bool(a))
a = "" # 빈 문자열이면 false
print(bool(a))

# 리스트의 참 거짓
li = [1, 2, 3] # 있으면 true
li2 = [] # 없으면 false
print(bool(li))
print(bool(li2))

# 튜플의 참 거짓 
t1 = (1, 2, 3) # 리스트와 마찬가지로 있으면 true
t2 = () # 없으면 false
print(bool(t1))
print(bool(t2))

# 딕셔너리 참 거짓 
d1 = {'a' : 1, 'b' : 2} # 있으면 true
d2 = {} # 없으면 false
print(bool(d1))
print(bool(d2))

# 숫자형 자료형
int1 = 20 # 0 아니면 모두 true
int2 = 0 # 0 이면 false
int3 = -20 # 음수도 true
print(bool(int1))
print(bool(int2))
print(bool(int3))

# 집합은??
set1 = set([1, 2, 3]) # 있으면 true 
set2 = set() # 없으면 false
print(bool(set1))
print(bool(set2))

# None 은??
print(bool(None)) # None 데이터는 false

# boolean 형 데이터 활용하는 예
# 반복문 안에서 사용
a = [1, 2, 3, 4]
while a: # a 리스트가 true 인 상태일 동안
    print(a) # a 리스트를 출력 하고
    a.pop() # 끝 데이터를 하나씩 날려준다고 가정하자 
# a 리스트 데이터가 비어있게 되면 false 가 되고 자동으로 while 문이 끝나게 된다.

# boolean 조건문에서 활용 예
if []: # 빈 리스트가 false인 상태이다
    print("참") # if 문 뒤에 조건식이 true 이면 "참" 을 출력하고
else: 
    print("거짓") # if 문 조건식이 false 이면 "거짓" 을 출력한다.
# 해당 조건문의 조건식 인 빈 리스트는 false 이므로 "거짓"을 출력한다.
if [1,2,3]: # 
    print("참")
else: 
    print("거짓")
# 해당 조건문의 조건식 인 리스트는 값을 갖고 있기 때문에 true 이므로 "참" 을 출력한다.

# 불리안으로 형변환 
# 위에서 이미 사용했지만 (bool()) 로 감싸주면 형변환이 된다.
a = bool([1,2,3])
print(type(a))
print(a)
# 자바를 하다 파이썬으로 넘어와서 그런지 파이썬은 형변환 하기 너무 쉬운거 같다.