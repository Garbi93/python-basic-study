# 모듈을 다르게 사용하기??
# 모듈로부터 원하는 기능을 타겟팅 해서 불러오기
from mod1 import add # mod1 으로부터 add 만 가져오겠다.
print(add(1,2)) # mod1으로 부터 add 를 불러왔고 add로만 직접 사용하능하다.
# print(sub(1,2)) # add 만 호출 했기 때문에 사용 불가능하다.