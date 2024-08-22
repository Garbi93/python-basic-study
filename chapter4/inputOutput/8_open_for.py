# 파일 객체를 for문과 함께 사용하기??

f = open("C:/doit/새파일.txt", "r")
for line in f:
    print(line)
f.close()
# while문과 다르게 for 문에서는 파일 객체 자체를 리스트로 인식해줘서 파일의 길이를 인식해 주는거 같다.
# 조건문 따로 넣어 break 포인트를 넣을 필요 없다.