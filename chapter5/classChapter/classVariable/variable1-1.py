# 클래스 변수 
# 각각 객체를 생성한다면 변수를 따로 관리 하게 될텐데
# 각각 생성한 객체에서도 동일하게 적용하고 싶은 변수에 사용 한다??

# 활용
class Family:
    lastname = "김" # 이렇게 변수를 생성하면 class 공통으로 적용되게 된다.

a = Family()
b = Family()
c = Family()
# 이렇게 3 객체를 만들면

print(a.lastname)
print(b.lastname)
print(c.lastname)
# 3 객체의 lastname 모두 "김" 이 되어있다.

a.lastname = "박"
# 하지만 따로 수정해서 관리도 가능하다.
print(a.lastname)
print(b.lastname)
print(c.lastname)
# 바꾼 사람만 바뀐다.
# 하지만 class 에서 직접 바뀐다면 전체에 영향을 받는다.