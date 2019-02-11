sum = 0
n = int(input('합계를 구할 수를 입력하세요 : '))

for i in range(n) :
    sum = sum + (i+1)

print('1부터 {}까지의 합은 {}'.format(n,sum))

