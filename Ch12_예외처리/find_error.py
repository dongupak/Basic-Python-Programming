try:
    b = 2 / 0
    a = 1 + "some"
except Exception as e:
    print('error',e)