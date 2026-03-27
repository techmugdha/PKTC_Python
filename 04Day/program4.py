class Student:
  '''Holds all data regarding student entity'''
  # ctor
  def __init__(self):
    print('Parameterless ctor of Student class')
    
  # def __str__(self):
  #   return "This is info about student class object...."
  
  def __repr__(self):
    return "This is info about student class object...."
    
  # method
  def display(self):
    print("displaying student data!!")
    print(self)
  

obj = Student() # Parameterless Contructor
obj.display()
# Student.__init__(obj)
# print(obj)
# print(obj.__doc__)