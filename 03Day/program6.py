def function1(func):
  print('Function1 output')
  func()

def function2(param, func):
  print('Function1 output')
  func(param)
 
def show():
  print('Show function output')  
  
def greet(name=''):
  print(f'hello {name}')

# function1(show)

function2('Tony Stark',greet)
