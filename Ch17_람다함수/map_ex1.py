a = [1, 2, 3, 4, 5, 6, 7]
square_list = map(lambda x: x**2, a)
cubic_list = map(lambda x: x**3, a)

for n in square_list:
    print(n,end=',')

print()
for n in cubic_list:
    print(n, end=',')


