# Open/closed Principle: Your entity closed for modification , but open for extention
# Decorator: based on Closure - child function is dependent on parent function data, child function should return from parent function

def mydecorator(func):
  def wrapper():
    print("Some change before calling display function")
    func()
    print("Some change after calling display function")
  return wrapper

@mydecorator 
def display():
  print("Some thing to display on UI")
   
display()
# inner = mydecorator(display)
# inner()