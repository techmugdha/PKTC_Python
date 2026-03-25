# Variable length Positional argumentss
def addition(*args):
  # print(type(args)) # tuple
  sum = 0
  for n in args:
    sum += n
  print(f"addition : {sum}")
  
# addition()  
# addition(1,2)
# addition(1,2,3)
# addition(1,2,3,4)
lst = [4,5,6]
# addition(*lst)
