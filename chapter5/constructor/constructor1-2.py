# 생성자 사용하기

class FourCal:
    def __init__(self, first, second): # 해당 변수가 생성자이다.
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# a = FourCal()
# 생성자를 넣은 class 를 객체 생성하면 바로 오류가 출력된다 
# 그래서 객체 생성을 에초에 막아 이후에 생길 오류를 막아준다.
# 생성자가 들어있는 class 를 생성하기 위해서는

# 생성장 안에 인수를 넣어주어 생성하면 생성자가 문제없이 작동하게 된다.
a = FourCal(4,2) # 이런식으로 넣어주면 __init__ 안에 작동이하면서 문제없이 객체가 생성된다.
print(a.add())