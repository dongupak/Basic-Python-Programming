class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
print('v1 =',v1,', v2 =',v2)

v3 = v1 + v2  # Vector2D의 + 연산이 정의되지 않았다
print('v1 + v2 = ',v3)

