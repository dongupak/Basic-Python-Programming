str = "Programming"

# 자음이 나타날때만 출력하는 기능으로
for val in str:
    if val in ['a','e','i','o','u']:
        break # 모음일 경우 반복문을 종료한다
    print(val)

print("The end")

