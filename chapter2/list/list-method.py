# 리스트의 메서드 (기능)들 
# 리스트에 요소 추가 (append())
a = [1, 2, 3]
a.append(5) # append 기능을 사용하면 괄호 안에 있는 값을 제일 마지막에 인덱스 뒤에 넣어준다.
print(a)
a.append([4, 3]) # 리스트 안에 리스트 추가도 가능하다.
print(a)

# 리스트 정렬하기 (sort())
a = [1, 4, 3, 2]
a.sort() # sort 명령어를 쓰고 괄호 안에 아무것도 안 넣으면 작은것부터 큰 순으로 정렬해준다.
print(a)
a = ["a", "c", "b"]
a.sort() # 숫자 역시 오름차순으로 정렬해준다.
print(a)

# 배열 뒤집기 (reverse())
a = ['a' , 'c' , 'b']
a.reverse() # 단순 뒤집으면 
print("revers 기능만 사용: " + str(a)) # 정렬 없이 배열 순서만 뒤집어 준다.
a.sort()
a.reverse() # sort 한후 reverse 를 해주면 정렬 후 순서를 뒤집어 준다.
print("sort 후 revers 사용: " + str(a)) # 내림차순 으로 정렬 해준다.

# 인덱스 반환 (index())
a = [1, 2, 3]
print(a.index(3)) # 소괄호 안에 있는 값이 배열 안에 몇 번째 인덱스에 있는지 반환해준다 
print(a.index(1)) # 1 은 0번 인덱스 

# 리스트에 요소 삽입 (insert(,))
a = [1, 2, 3]
a.insert(1, ['a','b']) # insert(몇 번째 인덱스, 들어가는 값)
print(a) # insert 를 사용하면 배열의 원하는 위치에 값을 추가 할 수 있다.

# 리스트 요소 제거 (remove())
# remove 는 괄호 안에 넣은 값이 배열에서 처음 나올때만 삭제한다.
a = [1, 2, 3, 1, 2, 3]
a.remove(3) # 처음 나오는 3 만 지운다.
print(a)

# 리스트 요소 끄집어 내기 (pop())
# remove와 비슷하다 리스트의 제일 마지막만 날려버린다.
a = [1, 2, 3, 4]
print(a.pop()) # pop 할때 print 를 쓰면 어떤것을 날리는지 볼 수 있다.
print(a)
print(a.pop(1)) # pop 안에 인덱스 값을 넣으면 해당 인덱스 값을 날린다.
print(a)

# 리스트 갯수 세기 (count())
a = [1, 2, 3, 1, 1]
print(a.count(1)) # count 의 괄호 안에 있는 값이 배열에 몇개가 존재하는지 출력해 준다.

# 리스트 확장 (extend())
a = [1, 2, 3]
a.extend([4, 5]) # append 와 다르게 인덱스에 배열이 통으로 값으로 들어가는게 아니라, 추가하는 값 만큼 인덱스도 추가해준다.
print(a)