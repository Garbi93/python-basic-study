# while 문의 맨 처음으로 돌아가기
# while 문을 사용하다 보면 while문을 빠져나가지 않고 
# 맨 처음으로 다시 돌아가게 하고 싶을때 사용한다.
# countinue 를 사용하여 특정 조건을 건너뛰게 하는거 같다 
# pass 랑 비슷 한거 같은데?? 다르다 pass 의 경우 while 문 안에서 이후 로직이 정상 수행 되지만
# countinue 의 경우 이후 로직 수행을 무시하고 다시 처음으로 올린다.
# countinue 는 자기를 바로 감싸는 한 while문 안에서만 작동한다.

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue # 짝수라면 countinue 를 만나서 처음으로 돌아가라
    print(a)