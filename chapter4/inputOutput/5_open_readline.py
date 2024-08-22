# 파일을 읽는 여러 가지 방법

# readline 함수를 사용 하기 
f = open("C:/doit/새파일.txt", 'r') 
# 두번째 인자에 r 을 사용하여 텍스트 문서 내의 파일을 읽겠다고 선언한 것
line = f.readline() 
# 텍스트 파일에서 갖고 온 내용 중 처음 만나는 한 줄 을 갖고 온다.
print(line)
f.close()
print("==========================================")

# 여러 줄 을 읽게 하려면??
# while 문을 사용하여 텍스트 문장이 끝날때까지 켜준다.
f = open("C:/doit/새파일.txt", 'r') 
while True:
    line = f.readline()
    if not line: 
        break
    print(line, end="") # 한줄씩 더 떨어지는게 싫다면 end 를 추가해주자.
f.close()
# 이상한건?? 텍스트 상 엔터를 코드에서 읽어 들어오기 때문에 코드출력해보면 줄마다 한 줄씩 더 띄어서 보이게 된다.