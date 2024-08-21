# 이중 for 문을 사용하여 
# 구구단 만들기
for i in range (2,10):
    print("%d 단을 실행합니다." % i)
    for j in range (1,10):
        print ("%d x %d = %d" % (i,j,i*j), end="|") # 여기서 end 를 쓰고 공백을 주면 print 출력후 줄 바꿈대신 공백으로 구분해준다는 것이다.
    print() # 내부의 for 문이 종료 되면 줄바꿈을 실행 시키기 위해 