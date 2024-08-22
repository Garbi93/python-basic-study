# 프로그램 입력 예제)

import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
# 받은 인수 들을 다 대문자로 바꿔 주고 줄 바꿈 하지 안고 한칸씩 띄어 출력해주기 
