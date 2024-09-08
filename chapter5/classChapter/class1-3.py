class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator() # 각각 계산기마다 다른 객체를 생성
cal2 = Calculator() # 클래스를 사용하는 변수는 각각 생성해주는건 같다.

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 이런식으로 사용하면 같은 함수를 반복적으로 생성하지 않고 
# 동일한 함수를 다른 객체로 생성하여 따로 관리 할수 있다.

# 클래스 계념 예
# class 는 붕어빵 틀
# 클래스를 사용해 생성한 객체는 붕어빵이 되는거다.
# 결국 class 는 동일한 작업을 하는 하나의 형태를 만들어 놓은것을 말한다.

"""
클래스는 반복되는 변수(값) & 메서드(함수)를
미리 정해놓은 틀(설계도) 이다. 
"""