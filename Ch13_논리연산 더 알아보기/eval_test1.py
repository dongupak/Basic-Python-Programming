def shortCircuitTest():
    print("shortCircuitTest()가 실행됨")
    return True

# 아래 문장의 조건1이 참이므로 조건2을 실행한 후 판단
if True and shortCircuitTest():
    print("참일때 실행!")
else:
    print("거짓일때 실행!")

