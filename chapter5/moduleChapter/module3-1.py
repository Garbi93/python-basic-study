# 모듈위치를 찾아오게 하기
import sys 
sys.path.append("C:/python") # 찾을 경로를 입력해주면 찾을 수 있다.

import mod3 as m # mod3 를 as 를 사용 하여 줄여쓸 수도 있다.

a = m.Math()
print(a.solv(2))