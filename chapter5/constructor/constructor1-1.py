# 생성자 

# 생성자는 class 를 호출하자마자 작동하는 것을 말한다.

# 우리가 만든 FourCal 클래스를 다음과 같이 사용해 보자
class FourCal:
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
    
a = FourCal()
# a.add() # add 기능을 바로 사용하려하면 setdata 로 들어온 값이 없어 에러가 발생하게 된다.
# 이와 같은 오류를 막기 위해 메서드를 호출하는것보다 객체를 생성할때에 바로 작동하는것이 생성자
# 고 생성자를 사용하여 오류를 막아주면 된다.

# __init__ 을 파이썬 메서드명으로 사용하면 해당 메서드는 생성자가 된다.