# 코드를 쓸 때 계속 따옴표가 나오면 번거로우니 자주 사용되는 값에 이름을 붙입니다.
SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이겼다!'
DRAW = '비겼다'
LOSE = '졌다...'

# 내가 낼 패와 상대가 낼 패 결정
mine = SCISSOR
computer = ROCK

if mine == computer:
    result = DRAW
else:
    if mine == SCISSOR:
        if computer == PAPER:
            result = WIN
        else:  # yours = 바위
            result = LOSE
    elif mine == ROCK:
        if computer == SCISSOR:
            result = WIN
        else:
            result = LOSE
    else:
        if mine == PAPER:
            if computer == ROCK:
                result = WIN
            else:
                result = LOSE

print(result)
