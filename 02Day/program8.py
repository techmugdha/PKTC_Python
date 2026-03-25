# dictionay {'key':'value',}

shopping_cart = {'apple':100,'banana':60, 'orange':120}
sum = 0
# for key in shopping_cart:
#   sum += shopping_cart[key]
  # print(key,shopping_cart[key])
  
# print(f'total: rs.{sum}')
  
# keys:
# print('keys',list(shopping_cart.keys()))
# print('values',shopping_cart.values())

# Dictionary Destructing Syntax
for item in shopping_cart.items():
  print(item)
  
for key,value in shopping_cart.items():
  # print(key,value)
  sum += value
  
print(f'total: {sum}')