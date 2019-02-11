import datetime as d

today = d.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year,\
                                  today.month,today.day))

xMas = d.datetime(2018, 12, 25)
leftTime = xMas - d.datetime.now()

print('다음 크리스마스 까지는 {}일 {}시간 남았습니다.'.format(\
    leftTime.days,leftTime.seconds // 3600))

