import random

number = random.randint(1, 31) # number 라는 변수를 설정해 1에서 31 중에서 랜덤 숫자를 꺼냄
print(f' 내 마음 속 숫자: {number}') # number 라는 랜덤한 숫자를 출력함
running = True # running 이라는 변수를 설정해 True 라고 정의

while running: # running 은 True 이기 때문에 True 일 경우 (즉, 끊임없이) 반복해서 돌아감
    guess = int(input('1~31 중 내가 생각한 숫자는?')) # 입력받은 값을 정수(int) 로 변환하여 guess 에 대입
    print(f'입력받은 숫자: {guess}') # guess 라는 변수 (내가 추측하는 숫자)를 출력함

    if guess < number: # 내가 생각한 숫자보다 랜덤한 숫자가 클 경우
        print(f'{guess}보다 큽니다.') # 랜덤한 숫자가 내가 생각한 숫자보다 크다고 출력
    elif guess > number: # 내가 생각한 숫자보다 랜덤한 숫자가 작을 경우
        print(f'{guess}보다 작습니다.') # 랜덤한 숫자가 내가 생각한 숫자보다 작다고 출력
    else: #내가 생각한 숫자보다 랜덤한 숫자가 같을 경우
        print(f'내가 생각한 숫자가 맞습니다.') # 랜덤한 숫자가 내가 생각한 숫자와 같다고 출력
        running = False # running = True 라고 위의 정의했기에 계속 돌아가는 것. 그래서 숫자를 맞췄을 때 멈추려면 running = False 라고 해야지만 while 반복문이 멈춤. 그리고 게임이 끝남.