class Demo:
  def instance_method(self):
    print(f"this is instance method: {self}")
   
  @classmethod  
  def class_method(cls):
    print(f"this is class method : {cls}")
  
  # When you have to attach extra functionality with class which is not directly realted to current purpose of the class
  @staticmethod  
  def static_method():
    print("this is static method")
    
obj = Demo()
obj.instance_method()
Demo.class_method()
Demo.static_method()

obj2= Demo()