import datetime as d

print('오늘 =',d.datetime.now())

hundred = d.timedelta(days=100)
plus100Day = d.datetime.now() + hundred
print('100일 후=',plus100Day)

minus100Day = d.datetime.now() - hundred
print('100일 전=',minus100Day)

