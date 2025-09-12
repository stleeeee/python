# dictionary 는 key:value 형태로 되어있다.'
# 비슷한 자료 구조로는 JavaScrip의 object, Java의 map 이 있다.
dic1 = {'name':'kim,ji-hoon', 'phone':'010-1234-1234', 'age':55}
dic2 = {'name':'hong,gil-dong', 'phone':'010-2233-5454', 'friends':['Alice', 'John', 'Smith']}

# 사전에 데이터 넣기 1
a = {'first':'a'}
print(a)

# 사전에 데이터 넣기 2
a['second'] = 'b'
print(a)

# 사전에서 특정 요소 삭제
del a['second']
print(a)