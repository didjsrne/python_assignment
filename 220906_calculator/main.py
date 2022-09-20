from calculate import cal_result

num1 = int(input('첫번째 숫자를 입력: '))
num2 = int(input('두번째 숫자를 입력: '))
op = input('연산자를 입력: ')
print(f'{num1} {op} {num2} = {cal_result(num1, num2, op)}')