import math

class Cylinder:

  def __init__(self, radius, height):
    self.radius = radius
    self.height = height

  def get_radius(self):
    return self.radius

  def set_radius(self, radius):
      if radius>0:
        self.radius = radius

  def get_height(self):
    return self.height

  def set_height(self, height):
    if height>0:
      self.height = height

  def calc_bottom_area(self):
    return (self.radius * math.pi)**2

  def calc_surface_area(self):
    return (2*math.pi*self.radius)*self.height
  
  def area(self):
    return 2*((self.radius*math.pi)**2) + (2*math.pi*self.radius)*self.height


 



