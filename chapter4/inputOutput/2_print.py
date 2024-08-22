# print 자세히 알기 

print("life" "is" "too short") # 1번
print("life" + "is" + "too short") # 2번
# 1번과 2번이 동일하게 출력 된다.
# 단 같은 자료형일때만 더해준다.
# 문자열간 띄어쓰기를 하고 싶으면 , 로 구분하면 띄어쓰기를 하여 더해준다.
print("life" , "is" , "too short") # 3번

# 이전에도 했지만 
# 한줄 띄기가 아닌 한칸 띄기
for i in range(0, 10):
    print(i)
# 원래는 이런식으로 print 당 줄을 나누어 주지만
print()
for i in range(0, 10):
    print(i, end=" | ")
# print 문 안에 end="사이에 넣고싶은 구조" 를 넣으면 줄 나눔 없이 나열하는 식으로 출력해준다. 
