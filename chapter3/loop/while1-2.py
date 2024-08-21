# while 문을 사용하여 프롬프트 만들어보기

prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input()) # 오 파이썬은 인풋을 이렇게 받는듯 하다.
