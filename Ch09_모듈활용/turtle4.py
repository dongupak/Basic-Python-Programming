import turtle as t

t.shape("turtle")
t.color("blue")
t.circle(80)

t.forward(160)
t.color("green")
t.circle(80)

t.color("red")
t.pensize(3)
t.lt(90)
for i in range(6):
    t.forward(60)
    t.left(60)

t.done()

