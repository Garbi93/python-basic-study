# 상속 추가 활용
class FourCal:
    def __init__(self, first, second): 
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
    
# 계산기 상속 받은 계산기 만들기 ----------------------
class MoreFourCal(FourCal):
    def pow(self): # first 를 second 제곱 기능 추가
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
print(a.add()) # 부모 기능
print(a.pow()) # 자신 기능