# 메서드 오버라이딩
# 자바에서도 배웠지만
# 물려받은 기능을 새로운기능으로 덮어 씌우는것을 말한다.


# 오버라이딩 예
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
    
# 계산기 상속 받은 계산기 오버 라이딩 활용해보기 ----------------------
class SafeFourCal(FourCal):
    def div(self): # 부모 div 를 무시해버리고 자신의 div로 덮어씌우게 된다.
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.div()) # 부모것을 썻다면 에러가 나겠지만 자신것을 사용하면 0이 에러없이 출력된다.