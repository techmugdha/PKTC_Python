# Higher Oder functions:
# lambda / Anonymous function
# def double(num):
#   return num * 2

double = lambda num: num * 2
# print(double(3))

greet = lambda :print('Hi there!!!')
# greet()

# display = lambda nm: print(f'your name is : {nm}')

# display('Hugh')

# (lambda nm: print(f'your name is : {nm}'))(input('Enter your name: '))

lst = [1,2,3,4,5]
newlst = map(double,lst)
# print(list(newlst))

newlst1 = map(lambda num: num * num,lst)
# print(list(newlst1))

# for nm in range(0,11):
#   print(nm)

numbers = list(range(1,11))
print(numbers)
