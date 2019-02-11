str = "Programming"

# 모음이 나타나면 출력을 건나뛴다
for val in str:
    if val in ['a','e','i','o','u']:
        continue # 모음일 경우 출력을 하지않고 다음으로 넘어간다
    print(val)

print("The end")

