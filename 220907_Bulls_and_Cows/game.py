import random
import time
from datetime import datetime

start_time = time.time()  # 시작 시간 세팅

def generate_numbers():  # 난수 생성
    global count  # 몇 자리 수인지를 전역변수로 설정
    numbers = []
    while True:
        count = int(input('몇 자리 숫자로 플레이 할지 입력 : '))
        if count < 3:
            print("3 이상의 값을 입력해주세요")
            continue
        if count > 10:
            print("10 이하의 값을 입력해주세요")
            continue

        while len(numbers) < count:
            num = random.randint(0, 9)  # 랜덤 변수 생성
            if num not in numbers:  # 리스트 안에 없다면
                numbers.append(num)  # 추가하는 식으로 변수중복 차단

        print(f"0과 9 사이의 서로 다른 숫자 {count}개를 랜덤한 순서로 뽑았습니다.\n")
        return numbers  # 함수 generate_numbers() = numbers 정답지 리스트

def take_guess():  # 내 답안지
    print(f"숫자 {count}개를 하나씩 차례대로 입력하세요.")
    i = 0
    new_guess = []
    while i < count:  # count 수까지 반복
        gue_number = input(f"{i + 1}번째 숫자를 입력하세요: ")
        if gue_number == "exit":
            print("게임을 종료합니다.")
            exit()
        if int(gue_number) > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if int(gue_number) in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요. ")
            continue
        else:  # 문제 없으면
            new_guess.append(int(gue_number))  # 답안지 리스트에 적고
            i += 1  # 다음번호로

    return new_guess  # 함수 take_guess() = new_guess 내 답안지


def get_score(guess, solution):  # 답안지를 정답과 비교하기
    strike_count = 0
    ball_count = 0
    i = 0

    while i < count:
        if guess[i] == solution[i]:  # 숫자가 리스트 순서까지 같다면 스트라이크
            strike_count += 1
            i += 1
        elif guess[i] in solution:  # 숫자가 리스트 안에 존재한다면 볼
            ball_count += 1
            i += 1
        else:  # 아니면 뭐 없지
            i += 1

    return strike_count, ball_count  # get_score 함수는 (스트라이크, 볼) 카운트


# 여기서부터 게임 시작!
ANSWER = generate_numbers()  # 내 답안지
tries = 0  # 시도 횟수

while True:
    GUESS = take_guess()  # 내 답안지
    strike, ball = get_score(GUESS, ANSWER)
    print(f"{strike}S {ball}B ")

    if strike == count:  # 정답이라면
        tries += 1  # 시도는 한번 올리고
        end_time = time.time()  # 마무리 시간 재고
        print(f"정답입니다! 시도:{tries}회 소요시간:{end_time-start_time:.2f}초 {datetime.now()}")  # 시도 횟수, 걸린 시간, 맞춘 시점 시간까지 보여주고
        break  # 끝
    else:
        tries += 1  # 시도 횟수 하나 올리고 다시