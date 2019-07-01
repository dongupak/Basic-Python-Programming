class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_vec):
        return Vector2D(self.x + other_vec.x, self.y + other_vec.y)

    def __sub__(self, other_vec):
        return Vector2D(self.x - other_vec.x, self.y - other_vec.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __str__(self):
        return "({},{})".format(self.x, self.y)

v1 = Vector2D( 30, 40 )
v2 = Vector2D( 10, 20 )
print('v1 =',v1,', v2 =',v2)

v3 = v1 + v2
print('v1 + v2 = ',v3)
v4 = v1 - v2
print('v1 - v2 = ',v4)
print('-v1 = ',-v1)

