# singleton:
class Singleton:
  _instance = None
  # __new__ magic method creats new object of our class  
  def __new__(cls,*args,**kwargs):
    if cls._instance is None:
      print('Creating new instance...')
      cls._instance = super().__new__(cls)  
    return cls._instance
      
  # __init__ will intialize this newly created object.
  def __init__(self,value):
    # print('Initializing Object with some values..')
    self.value = value
  
s1 = Singleton(10)
s2 = Singleton(20)

print(s1.__dict__)
print(s2.__dict__)

