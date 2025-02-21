import math
class VectorNd:
  def __init__(self, *args):
    self.args = list(args)
  def __str__(self):
    return f"Vector{tuple(self.args)}"
  def __add__(self, other):
    try:
      return VectorNd(*[a + b for a, b in zip(self.args, other.args)])
    except AttributeError:
      print("Error: Cannot add Vectors of different dimensions")
    except ValueError:
      print("Please enter a number for the dimensions of vector")
  
  def __sub__(self, other):
    try:
      return VectorNd(*[a-b for a, b in zip(self.args, other.args)])
    except AttributeError:
      print("Error: Cannot sub Vectors of different dimensions")
    except  ValueError:
      print("Please enter a number for the dimensions of vector")
  def __mul__(self, other):
    try:
      if isinstance(other, VectorNd):
        return sum([a*b for a, b in zip(self.args, other.args)])
      elif isinstance(other, (int, float)):
        return VectorNd(*[a*other for a in self.args])
    except AttributeError:
      print("Error: Cannot mul Vectors of different dimensions")
    except  ValueError:
      print("Please enter a number for the dimensions of vector")

  def __rmul__(self, other):
   return self.__mul__(other)

  def magnitude(self):
    return round((math.sqrt(sum([i**2 for i in self.args]))), 2)

  def normalize(self):
      return VectorNd(*[i/self.magnitude() for i in self.args])

v1 = VectorNd(1, 2, 3)
v2 = VectorNd(4, 5, 6)
v3 = v1 + v2
print(v3)
v4 = v1 - v2
print(v4)                    
v5 = v2 * v1
print(v5)                 
v6 = 2*v1
print(v6)
print(v1.magnitude())
print(v1.normalize())

