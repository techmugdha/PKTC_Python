# 3. A function in python can return another function.

def addition(n1,n2):
  return n1+n2

# addresult = addition(2,3)
# print(f"Add result  = {addresult}")

def parent():
  print('This is parent function output!')
  def child():
    print('This is child function output!')
  return child

# inner_function = parent()
# inner_function()

def outer1(name):
  # name parameter is local to : outer1
  def inner1():
    print(f"Hello, {name}!")
  return inner1

# inner = outer1('Hugh Jackman')
# inner()
num = 0
def counter():
  def count(nm):
    nm += 1
    print(nm)
  return count

count = counter()
# count(num)
# count(num)
