def raiseError(inNum):
    arr = [1,2,3]
    if inNum in arr:
        print("정상적인 입력입니다.")
    else:
        raise ValueError("입력값을 다시 확인하세요")

while(True):
    try:
        inNum = int(input("1,2,3중 하나를 선택하세요 "))
        raiseError(inNum)
        break
    except Exception as e:
        print('error',e)

