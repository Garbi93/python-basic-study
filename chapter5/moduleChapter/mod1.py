def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print(__name__) # 이건 불러오는 곳마다 mod1이 출력된다. 

# 만약 다른데서 호출했을때 print 가 되는 불상사를 막고싶다면
# __name__ 을 사용하여 막아준다

if __name__ == "__main__": # 이렇게 해주면 자신만 실행할때 보이지만 외부에서 가져다 쓸때는 보이지 않는다.
    print(add(1,2)) 