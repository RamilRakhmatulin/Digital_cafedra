class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return Vector(sum_x, sum_y)
    def __sub__(self, other):
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        return Vector(sub_x, sub_y)
    def __mul__(self, other):
        mul_x = self.x * other
        mul_y = self.y * other
        return Vector(mul_x, mul_y)
    def __str__(self):
        return  f"({self.x}, {self.y})"

vector1=Vector(2,3)
vector2=Vector(3,2)
vec3=vector1-vector2
print(vector1+vector2)
print(vec3)
print(vec3*0.5)