def adult_func(n):
    if n >= 19:
        return True
    else:
        return False


ages = [34, 39, 20, 18, 13, 54]

print('성년 리스트 :')
for a in filter(adult_func, ages):
    print(a)

