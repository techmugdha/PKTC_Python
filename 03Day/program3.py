# 2. A function in python can be nested inside another function

def parent():
  print('Hi from Parent function')
  def child():
    print('Hello from Child function')
  child()
    
# parent()

def outer1(name):
  # name is local variable : outer1
  def inner1():
    print(f"Hello, {name}!")
  
  inner1()

# outer1('Hugh Jackman')

def outer2():
  num = 100 # local scope
  print(dir())# ['num']
  
  def inner2():
    age = 18
    print(dir()) #['age']
    
  inner2()
  print(dir())# ['inner2','num']
    
# outer2()
    