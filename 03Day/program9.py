# generator:are a special type of iterable,just like tuple, list.

lst = [1,2,3,4,5] # iterable
# for n in lst:
#   print(n)

iter_obj = iter(lst)
# print(iter_obj,type(iter_obj))

n1 = next(iter_obj) #1
print(n1)
n2 = next(iter_obj)#2
print(n2)
n3 = next(iter_obj)#3
print(n3)
n4 = next(iter_obj)#4
print(n4)
n5 = next(iter_obj)#5
print(n5)
n6 = next(iter_obj)# StopIteration
print(n6)