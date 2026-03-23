def function1():
  print("{} - {} - {}".format(10,20,30))
  print(f"{10} - {20}")
  
# function1()

def function2():
  # Positive index based collection
  lst = [1, 2, 3, 4, 5]
  print(lst[0])
  print(lst[1])
  print(lst[2])
  print(lst[3])
  print(lst[4])

# function2()

def function3():
  # Negative index based collection
  lst = [1, 2, 3, 4, 5]
  print(len(lst))
  print(lst[-1])
  print(lst[-2])
  print(lst[-3])
  print(lst[-4])
  print(lst[-5])

# function3()

def function4():
  l1 = [1,2,3,4,5]
  l2 = [6,7,8]
  # lst = l1 + l2
  # print(lst)
  lst = l1[2] + l2[-2]
  print(lst)
  
# function4()
  
def function5():
  l1 = [11,12,13]
  l2 = [11,12,13]
  l3 = []
  l4 = []
  
  print(l1, type(l1),id(l1))
  print(l2, type(l2),id(l2))
  print(l3, type(l3),id(l3))
  print(l4, type(l4),id(l4))
 
# function5() 

def function6():
  lst = [1,2,3,4,5,6,7,8,9,10]
  # slicing
  print(lst)
  print(lst[0:5])
  print(lst[-5:-1])
  print(lst[-5:])
  print(lst[1::2])
  
# function6()

def function7():
  shopping_list = []
  choice = ''
  while True:
    item = input("Enter name of purchased item: ")
    shopping_list.append(item)
    print(f"You have purchased {len(shopping_list)} items, {shopping_list}")
    print("Do you want to continue? 'y'/'n'")
    choice = input().lower() # Y, N, y, n
    if choice == 'n':
      print('Thank you .. visit again!!')
      break
  
# function7()

def function8():
  str = '  hello  '
  # print(str[-1])
  # print(str[0])
  # print(str[0:3])
  print(10,str.strip(),20)
  print(10,str.lstrip(),20)
  print(10,str.rstrip(),20)
  
  names = 'Tim, Rob'
  lst_names = names.split(',')

function8()
