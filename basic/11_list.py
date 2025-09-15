# 파스칼 표기법 - 맨 앞글자만 대분자(Java 의 class 생성 시 활용)
# 카멜 표기법 - 단어의 의미가 있는 첫글자를 대문자로 한다. (shopList)
# 스네이크 표기법 - 단어간의 구분을 _로 한다. (shop_list)

# 리스트 생성 방법 1 - 비어있는 리스트로 생성
a = []

# 리스트 생성 방법 2 - 값이 있는 리스트로 생성
shop_list = ['apple', 'mango', 'carrot', 'banana']
print(f'shop list: {shop_list}')

# 리스트에 값을 넣는 방법
# 가장 뒤로부터 넣는 방법
a.append(1)
a.append(2)
a.append(3)
# 틀정한 번호를 지정해서 넣는 방법
a.insert(1, 'X')

print(f'a의 길이: {len(a)}')
print(f'a: {a}')

# a 의 2번방에 있는 값
print(f'a[2]={a[2]}')
# a 의 마지막에 있는 값
print(f'a의 마지막 방의 값 = {a[3]}')
# 길이에서 1을 뺀 값을 이용 -> 인덱스는 0번부터 시작한다는 점을 이용
print(f'a의 마지막 방의 값 = {a[len(a)-1]}')
# 파이썬에서 사용되는 방식, 0보다 뒤로가면 맨 뒤로 이동된다는 개념
print(f'a의 마지막 방의 값 = {a[-1]}')

# 리스트 정렬(sort)
shop_list.sort() # 오름차순
print(f'shop_list: {shop_list}')

shop_list.sort(reverse=True) # 내림차순
print(f'shop_list: {shop_list}')

# sorted 는 원본의 리스트를 정렬한 값을 새로운 리스트로 반환
new_list = sorted(shop_list)
print(f'new_list: {new_list}')

# a의 2 번 인덱스에 c 를 놓는다.
# insert 와 다른점은 해당 인덱스의 값을 지우고 새로 넣는다는 것이다.
a[2] = 'c'
print(f'a: {a}')

#list 삭제
del a[1]
print(f'a: {a}')