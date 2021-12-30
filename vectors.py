from math import sqrt

class Vector:

  def __init__(self, name, x, y, z):
      self.name = name
      self.x = x
      self.y = y
      self.z = z
      self.length = sqrt(self.x**2+self.y**2+self.z**2)
  def __str__ (self):

    return f"x: {self.x}, y: {self.y}, z: {self.z}"
  
  def __len__ (self): # целая часть значения длины
    self.length = int (sqrt(self.x**2+self.y**2+self.z**2))
    return self.length

  def __add__(self, other):
    if type(other) == str or type(other) == int :
      print('Ошибка')
      return self
    else: 
      self.x= self.x + other.x
      self.y= self.y + other.y
      self.z= self.z + other.z

      return self

  def __sub__(self, other):
    if type(other) == str or type(other) == int :
      print('Ошибка')
      return self
    else: 
      self.x= self.x - other.x
      self.y= self.y - other.y
      self.z= self.z - other.z
      return self  

  def __mul__(self, other):

    if type(other) == str  :
      print('Ошибка')
      return self
    elif type(other) == int :
      self.x1 = self.x* other
      self.y1 = self.y* other
      self.z1 = self.z*other
    else: 
      self.x1 = self.y* other.z -self.z* other.y
      self.y1 = -(self.x* other.z -self.z* other.x)
      self.z1 = self.x*other.y - self.y * other.x

    self.x= self.x1
    self.y= self.y1
    self.z=self.z1
    return self

  def __radd__(self, other):
      self.__add__( other)

      return self

  def __rsub__(self, other):
    if type(other) == str or type(other) == int :
      print('Ошибка')
      return self
    else: 
      self.x= other.x - self.x 
      self.y= other.y - self.y
      self.z= other.z - self.z
      return self  
  def __rmul__(self, other):

    super().__mul__(other)
    self.x = -self.x1
    self.y = -self.y1
    self.z = -self.z1
    return self

  def __imul__(self, other):
    self.__mul__( other)
    return self
    
  def __iadd__(self, other):
      self.__add__( other)
      return self

  def __isub__(self, other):
    self.__sub__( other)
    return self

  def __pow__(self, other):

    self.x = self.x**other
    self.y = self.y**other
    self.z = self.z**other
    return self

  def __eq__(self, other):
    if self.length == other.length :
      print ('равны')
    else:
      print (' не равны')

  def __ne__(self, other):
    if self.length != other.length :
      print ('не равны')
    else:
      print (' равны')


a= Vector('a', 3,7,6)  
b = Vector('b', 6,7,8) 
c = Vector('c', 2,3,4)
d = Vector('c', 1,2,3)
f = Vector('c', 1,2,3)
print (len(a))

d==f
d += f 
print (d)
d= d+ f
print (d)
d= d-f
print (d)




a= a*b
print (a)
c= b*c
print (c)

c= a-c
print (c)
c= a+c
print (c)

c!=b

b *= d
print (c)
c-=f
print (c)

a = a + 5 
b= b + '5'
a = a - 5 
b= b - '5'
c= c* 'e'