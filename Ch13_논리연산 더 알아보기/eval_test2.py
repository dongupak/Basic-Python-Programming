def shortCircuitTest():
    print("shortCircuitTest()가 실행됨")
    return True

# 아래 문장의 조건1이 거짓이므로 조건2을 실행하지 않고 판단
if False and shortCircuitTest():
    print("참일때 실행!")
else:
    print("거짓일때 실행!")
