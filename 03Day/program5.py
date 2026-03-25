# 4. A function can be passed as a parameter to another function
num = 9
def check(num):
  if(num> 10):
    print(f'{num} is grater than 10')
  else:
    print(f'{num} is less than 10')
    
# check(num)

# DRY Principle
# SRP
def passstud(marks):
  print(f"Congratualtions! you have passed with {marks} marks!!")
  
def failstud(marks):
  print(f"Congratualtions! you have failed with {marks} marks!!")
  
def smsstud(marks):
  print(f"SMS sent about result!")
  
def emailstud(marks):
  print(f"Email sent about result!")
  
def calculate_result(marks,passfunc,failfunc):
  if(marks >= 40):
    passfunc(marks)
  else:
    failfunc(marks)
    
mk = int(input("Enter your marks: "))
# calculate_result(mk)
ch = 2
if ch == 1:
  calculate_result(mk,smsstud,failstud)
elif ch == 2:
  calculate_result(mk, passstud, emailstud)
else:
  print('Pending result calculation')