# 제어문 영역에는 -> 조건문과, 반복문이 있다 
# 이번에는 조건문을 배울 예정 
# 조건문 (if)
# 돈이 있으면 택시를 타고, 돈이 없으면 걸어간다 와 같은 상황에 사용 된다.
# 어떤 조건을 기준으로 행동을 달리 해야할때 조건문을 사용한다.

# 조건문 사용 
money = False # 조건식 변수
if money: # 조건식이 들어가는 부분 
    print("택시 타고 가라") # 조건식이 true 상태이면 출력
else:
    print("걸어 가라") # 조건식이 false 면 출력

# if 문의 구조
"""
if 조건문:
    수행할 문장 1
    수행할 문장 2
    ...
else:
    수행할 문장 A
    수행할 문장 B
    ...
"""
# 이런형식이 기본 구조 이다.
# if 문에 속하는 문장은 들여쓰기를 해야한다.
# 파이썬에서는 들여쓰기가 중요하고 강제한다.
# 들여쓰기를 하지 않으면 indentationError 를 발생시킨다.

# 들여쓰기 차이 확인하기
money = True
if money:
    print("택시를")
    print("타고")
    print("가라")
# 해당 조건문은 money 가 true 이면 택시를 타고 가라를 다 출력 해주는 구문이고

if money:
    print("택시를")
print("타고")
print("가라")
# 해당 조건문은 money 가 true 이면 택시를 만 출력해주고 조건 문은 끝나게 되고 이후에 
# 그냥 print 문이 실행되어 타고 가라 가 연속해서 출력이 된다.

"""
if money:
    print("택시를")
print("타고")
    print("가라")
"""
# 해당 조건문은 택시를 과 타고 까지는 문제가 없지만 가라 부분에서 들여쓰기가 적용되 에러가 발생하게 된다.
# 조건 문 다음에 : 콜론을 잊지말고 사용해야 한다.

# 조건문 이란? 참, 거짓을 판단하는 문장을 말한다.

# 비교 연산자에서 true false 값은?? 
x = 3
y = 2
print(x > y)
print(x < y)
print(x != y)
print(x == y)

# 예제)
# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 않으면 걸어가라 
money = 2000
if money >= 3000:
    print("택시 타고 가기")
else:
    print("걸어가기")

# and, or, not 을 사용 하는 예제
# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라.
money = 2000
card = True
if money >= 3000 or card:
    print("택시 타고 가기")
else:
    print("걸어가기")
# 여기서 조건식에 여러 조건을 걸어 주고 싶다면 "or" 를 넣어서 추가로 조건식을 넣어줄 수 있다.

# x or y : x, y 둘 중 하나만 참이어도 참
# x and y : x, y 둘다 참이어야 참 하나라도 틀리면 거짓
# not x : x 가 거짓이면 참, x 가 참이면 거짓 

# and 해당 식은 둘다 참이어야 택시를 탈 수 있다.
money = 2000
card = True
if money >= 3000 and card:
    print("택시 타고 가기")
else:
    print("걸어가기")

# not 해당식은 조건식이 false 상태를 띌때 택시를 탈 수 있다.
card = False
if not card:
    print("카드 없을때 택시 타기")
else:
    print("카드 있으면 걸어가기")


# in, not in 
# ~ 안에 라는 식으로 이해하면 되는 조건 식이다. 
# 다른 프로그램 언어에서는 볼 수 없었던것
# x in 리스트 : x 가 리스트 안에 있을때 true
# x not in 리스트 : x 가 리스트 안에 있을때 false 
# 리스트 뿐 아니라, 튜플, 문자열도 in, not in 을 사용할 수 있다.
print("in 테스트")
list1 = [1, 2, 3]
print(1 in list1)
print("not in 테스트")
print(1 not in list1)
print("튜플 문자열로 in 테스트")
tu1 = ('a', 'b', 'c')
print('a' in tu1) # 있으니 true
print('j' not in tu1) # 없으니 true 
print("문자열 in 테스트")
str1 = "python"
print('p' in str1) # p 를 포함 하고 있어 true
print('p ' in str1) # 공백을 인식 하여 false 를 출력 

# 예제)
# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가기
pocket = ['money', 'card', 'phone']
if 'money' in pocket:
    print("주머니에 돈이 있어 택시 타고 가기")
else:
    print("돈이 없어서 걸어가기")

# 조건문에서 아무일도 발생하지 않길 바란다면??
# 비워두면 오류가 발생하기 때문에 pass 를 사용하여 건너뛰게 할수 있다.
print("패스 테스트 시작")
if 'money' in pocket:
    pass
else:
    print("패스 못함")
print("패스 테스트 끝")
# 특정 조건에서 아무것도 안하고 싶다면 pass 를 사용 하자

# 다양한 조건을 판단하는
# elif 
# 다른 언어에서는 else if 인거 같다.
# 예제)
# 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라
pocket = ['phone']
# 기존에는 이렇게 했다면 
if 'money' in pocket:
    print("돈이 있어 택시 타기")
else:
    if 'card' in pocket:
        print("돈은 없지만 카드가 있어서 택시 타기")
    else:
        print("돈도 카드도 없어서 걸어가기")

# elif 문을 사용하면 이렇게도 가능하다.
if 'money' in pocket:
    print("돈이 있어 택시 타기")
elif 'money' not in pocket and 'card' in pocket:
    print("돈은 없지만 카드가 있어서 택시 타기")
else:
    print("돈도 카드도 없어서 걸어가기")

# elif 는 갯수 제한 없이 사용할 수 있다.

# if 문 한줄로 줄여 쓰기
pocket = ['paper', 'money', 'cellphone']
print("줄여쓰기 전")
if 'money' not in pocket:
    pass
else:
    print("카드를 꺼내라")

print("줄여쓰기 후")
if 'money' in pocket: pass
else: print("카드를 꺼내라")
# 조건문의 조건과 결과를 : 콜론으로 구분 지으므로 줄여서 사용할 수 있다.
# 보통은 한줄로 쓰는건 구분하기 힘들어 나눠 쓰는것을 권장한다.

# 조건부 표현식
# 약간 패션 코드느낌이 든다.
score = 50
print("조건부 표현식 전")
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)
print("조건부 표현식 후")
message = "success" if score >= 60 else "failure"
print(message)
# 일단 message 변수에 "success" 라는 값을 넣고 score 가 60 이상이면 가만히 있고 else 일때 "failure" 가 message 변수에 들어가 출력 되게 된다.
# 정말 이상한거 많은 언어 인거 같다.