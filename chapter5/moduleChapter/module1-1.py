# 모듈 
# 우리가 직접 모듈을 만들일은 거의 없고 사용할일이 많다.
# 함수나 변수, 클래스를 모아 놓은 파이썬 파일을 말한다.

# 클래스는 찍어내는 개념이었다면
# 모듈은 불러오는 개념이라고한다.

# mod1 으로 만든것을 모듈로 불러와보자
import mod1 # 이렇게 다른곳에 있는 mod1 파일을 임폴트 시켜 가져오게 된다.
print(mod1.add(3,4))
