# docstring: documentation string: which tell extra information about function, classes, methods etc
def display():
  """This displays information about : Person"""
  # function body will go after this docstring
  print('Display info about a person')
  
display()
print(display.__doc__)
print(display.__name__)
print(__name__) # main module run : __main__