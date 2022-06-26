
class Line():
  
  def __init__(self, coord1, coord2):
    self.x1, self.y1 = coord1
    self.x2, self.y2 = coord2
    
  def distance(self):
    print(((self.x2-self.x1)**2 +(self.y2-self.y1)**2)**0.5)
    
  def slope(self):
    print(((self.y2-self.y1)/(self.x2-self.x1)))
    
    
    
class Cylinder():
  pi = 3.142
  def __init__(self, height=1, radius=1):
    self.height = height
    self.radius = radius
    
  def volume(self):
    print((Cylinder.pi * self.radius * self.radius * self.height))
    
  def surface_area(self):
    a1 = (2 * Cylinder.pi * self.radius * self.height)
    a2 = (2 * Cylinder.pi * self.radius * self.radius)
    print(a1 + a2)
    
    
li = Line((3,2), (8,10))

li.distance()
li.slope()

print('_' * 15)

c = Cylinder(2, 3)
c.volume()
c.surface_area()