lst = [3,2,4,1,5,6,7]
inNum = int(input("찾을 숫자를 입력하시오 : "))

i = 0
while i<len(lst):
    if lst[i] == inNum:
        print("%d번째 입니다."%(i+1))
        break
    print("탐색 중...")
    i+=1

