cnt = 0
while 1:
    a = input("문자 혹은 숫자를 입력 : ")
    if a == "exit":
        print("프로그램을 종료합니다.")
        exit()
    elif a.isdigit() == True:
        print(2*int(a))
        cnt += 1
        if cnt > 4:
            break
    elif a.isdigit() == False:
        print(f"입력한 문자는 {a}입니다.")
        cnt += 1
        if cnt > 4:
            break