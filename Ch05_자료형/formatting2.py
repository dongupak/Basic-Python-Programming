number = 20
greeting = '안녕하세요.'
place = '퐁당식당'
wait = '잠시만 기다려주세요.'

# 새로운 방법
base = '{} {}입니다. 손님의 대기 번호는 {}번 입니다. {}'
new_way = base.format(place,greeting,number,wait)

print(new_way)

