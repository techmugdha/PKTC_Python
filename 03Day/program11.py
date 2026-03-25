# Generator: 
def my_generator():
  yield "C++"
  yield "Java"
  yield "Python"

genrator_obj = my_generator()
print(next(genrator_obj))
print(next(genrator_obj))
print(next(genrator_obj))
print(next(genrator_obj))
