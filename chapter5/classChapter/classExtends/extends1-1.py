# 클래스의 상속
# 말그대로 부모 클래스의 기능을 자식 클래스가 물려받는다.
# 예를 들어 계산기를 만들었는데 
# 공학용 계산기를 추가로 만들라고 하면
# 기본 계산기 기능을 상속 받아 그대로 사용하고 추가 기능을 추가하면 된다.

# 상속 사용해보기

# 기본 계산기 ------------------------------------------------------------
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
class MoreFourCal(FourCal): # 부모 클래스를 인자 부분에 넣으면 상속 받게 된다.
    pass

a = MoreFourCal(4,1)
print(a.add()) # MoreFourCal 에는 add 가 없지만 상속받아 이렇게 사용이 가능하다.