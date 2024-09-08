# 모듈위치를 찾아오게 하기
import sys 
sys.path.append("C:/python") # 찾을 경로를 입력해주면 찾을 수 있다.

import mod3 # mod3 를 못 찾는다.

a = mod3.Math()
print(a.solv(2))