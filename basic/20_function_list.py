# 반환타입: O 매개변수: O - 자판기
# 반환타입: O 매개변수: X - 폴라로이드
# 반환타입: X 매개변수: O - 모금함
# 반환타입: X 매개변수: X - 리모컨

# 토스트기
def toaster(bread): # 선언: 만들어만놨지 누가 사용한건 아님
    print(f'{bread}이 구워지고 있다') # 실질적 동작이 아님, 사람 눈에만 보이는거
    return f'구워진 {bread}' # 실제로 밖으로 나오는 값

dish = toaster('식빵') # return으로 나온 값을 dish 에 담는다
print(dish) # dish 안의 값을 출력

# 자판기
def vending(card):
    print(f'{card}로 결제했다.')
    return f'{card}로 결제한 음료가 나왔다.'

card = vending('현대카드')
print(card)

# 폴라로이드
def polaroid():
    return '사진이 나왔다.'

photo = polaroid()
print(photo)

# 모금함
def box(cash):
    print(f'{cash}를 냈다.')

box('10000원')

# 리모컨
def remote():
    print('티비를 켰다.')

remote()