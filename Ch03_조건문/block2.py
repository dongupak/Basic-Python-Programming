num = -100

if num < 0:
    print(num, '은(는) 음수입니다')
else:
    print(num, '은(는) 음수가 아닙니다')
    # 짝수, 홀수는 음수가 아닌 경우에만 판별합시다
    if num % 2 == 0:
        print(num, '은(는) 짝수입니다')
    else:
        print(num, '은(는) 홀수입니다')