lst = [1,2,3,4,5]

def my_forloop(lst):
  itertor_obj = iter(lst)
  try:
    while True:
      element = next(itertor_obj)
      print(element)
  except StopIteration:
    # print('done with lst elements.. ')
    pass
    
my_forloop(lst)