height = 1.7
weight = 125

# bmi = 체중(kg) / 키(m)^2
bmi = weight / (height)**2

if bmi < 18.5:
    print ('저체중')
elif bmi < 23:
    print ('정상')
elif bmi < 25:
    print ('과체중')
else:
    print('비만')

