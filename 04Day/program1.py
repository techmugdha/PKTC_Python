# import sys
# # global / Module level namespace
# x = 100
# str = "Mugdha"

# def display():
#   print("display function")
  
# print(dir())
# print(sys.modules)

# ---------------------------
# num = 10 # global scope
def outer():
  # num =10 # local variable
  global num
  num += 2 
  print(num)
  def inner():
    print(num)
  inner()
  
# outer()
  
# -----------------------
x = 100 # global variable
# y = 12
def outer1():
  y = 20 # local variable
  def inner1():
    # global x
    str = 'something'# Enclosed Scope
    nonlocal y 
    y = y +10
    print(y)
    # print(dir())
  inner1()
  
outer1()