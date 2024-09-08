# 사칙연산 계산기 만들기

class FourCal:
    def setdata(self, first, second): # self 는 자기자신을 의미해서 매개 변수로 사용하지 않고 자신을 지칭한다
        self.first = first # 자신에 first 변수를 선언하고 매개변수로 들어온 first 를 넣어준다.
        self.second = second
        # 파이썬에서만의 특징으로 self 를 쓴다.
    
    # 더하기 기능
    def add(self):
        result = self.first + self.second
        return result
    
    # 곱하기 기능
    def mul(self):
        result = self.first * self.second
        return result
    
    # 빼기 기능
    def sub(self):
        result = self.first - self.second
        return result
    
    # 나누기 기능
    def div(self):
        result = self.first / self.second
        return result




a = FourCal() # 사칙연산 class 를 사용하는 객체 생성

a.setdata(4,2) # FourCal 클래스의 setdata 기능을 사용하여 변수 set 해주기
print(a.first) # self.first 로 저장한 4 가 출력 된다.
print(a.second)

print(a.add()) # FourCal 클래스의 add 기능을 사용하여 set 된 변수를 더해주기
print(a.mul()) 
print(a.sub()) 
print(a.div()) 

print("-" * 30)
# a 와 별도로 b 계산기를 각자 사용하여 따로 처리가 가능하다.
b = FourCal() # 사칙연산 class 를 사용하는 객체 생성

b.setdata(10,3) # FourCal 클래스의 setdata 기능을 사용하여 변수 set 해주기

print(b.add()) # FourCal 클래스의 add 기능을 사용하여 set 된 변수를 더해주기
print(b.mul()) 
print(b.sub()) 
print(b.div()) 