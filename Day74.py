#Method Overrriding
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
class Circle(Shape):
     def __init__(self,r):
         self.radius = r
         super().__init__(r,r)
     #def area(self):
         #return 3.14 * self.radius
    


rec = Shape(3,5)
print(rec.area())
c = Circle(5)
print(c.area())
