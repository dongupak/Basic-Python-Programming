import turtle as t

t.shape("turtle")
t.bgcolor("black")
t.color("green")
t.speed(0)  # 최고속도로 그림을 그린다

n = 20
for _ in range(n+1):
    t.circle(80)
    t.left(360.0/n)

t.done()
