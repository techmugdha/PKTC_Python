def display(firstname,lastname,age):
  print(f"Mr./Mrs. {firstname} {lastname} with age: {age}")
  
# display(lastname = 'Jackman',age=57,firstname='Hugh')

# variable length keyword arguments
def show(**kwargs):
  # print(type(kwargs))
  for key,value in kwargs.items():
    print(f"key= {key}, value= {value}")
  
show(apple=100,banana=60,orange=120)


  