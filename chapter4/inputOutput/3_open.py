# 파일 생성하기
# 종종 파일 생성해줄 일이 있어 자주 쓰인다.
# 웹 개발 할때 이미지 폴더 생성 해줄때 자주 했던거 같다.
# 이미지 생성할때도

f = open("새파일.txt", 'w') # open 을 사용하여 파일명과 확장자를 지정해주고 w 모드로 만들어주었다.
# 지금처럼 경로 지정 없이 사용하면 상대경로에 생성된다. 아마 지금 프로젝트 폴더 내에 생성 된거 같다.
f.close() # 사용하고 나선 기능을 닫아주기

# 사용 방법
# 파일_객체 = open(파일_이름, 파일_열기_모드)

# 파일 열기 모드 종류
# r : 읽기 모드 -> 파일을 읽을때만 사용
# w : 쓰기 모드 -> 파일에 내용을 쓸 때 사용
# a : 추가 모드 -> 파일의 마지막에 새로운 내용을 추가할 때 사용

# 파일 경로를 지정하여 생성해보기
f1 = open("fileCreateTestFolder/새파일.txt", 'w') # fileCreateTestFolder 경로에 새파일 텍스트 문서가 추가된 것을 볼 수 있다.
f1.close()

# 만일 절대 경로에 생성하고 싶다면 
# c:/ 를 사용하여 지정해주자.
# f2 = open("c:/createTest/새파일.txt", 'w') # 이런식으로 최상단 경로를 잡아 생성해주면 절대 위치에서 생성을 해준다.
# f2.close()

# 파일 경로 구분 방법
# / 단순 슬래시로 구분해줄 수 있지만, -> test/test2
# \\ 역 슬래시 2개로 구분 하여 사용해줄 수도 있다. -> test\\test2

# 주의 해야할 것은 파일 생성시 지정한 폴더가 없다면 파일 생성을 못한다.