# ConcreteImplementor 1/2
class DrawingAPI1:
    def draw_circle(self, x, y, radius):
        print('API1.circle(%d, %d, %d)' % (x, y, radius))

# ConcreteImplementor 2/2
class DrawingAPI2:
    def draw_circle(self, x, y, radius):
        print('API2.circle(%d, %d, %d)' % (x, y, radius))

# Refined Abstraction
class Circle():
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    # low-level i.e. Implementation specific
    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

shapes = [Circle(1, 2, 3, DrawingAPI1()), Circle(4, 5, 6, DrawingAPI2())]
for shape in shapes:
    shape.draw()
