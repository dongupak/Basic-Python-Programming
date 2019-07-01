# 출처
# https://www.w3schools.com/python/ref_func_filter.asp
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 20:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)

  