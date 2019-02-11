import math

def areaAndCircum(r): # 원 넓이, 둘레구하기,
    area = math.pi*r**2
    circum = 2*math.pi*r
    res = area, circum
    return res

radius = 4
area, circum = areaAndCircum(radius)
print('반지름',radius,'인 원의 면적과 둘레 :',area, circum)




