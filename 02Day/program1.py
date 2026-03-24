# Resuability, Do not repeat yourself (DRY) Principle
# Single Responsibilty Principle(SRP)
# In Python method overloadding is not allowed
def addition(n1,n2):
  print(n1+n2)
  
# addition(10,20)
# addition(2,3)

# Optional / Default Parameter
def addition(n1,n2,n3=0):
  print(n1+n2+n3)
  
  
addition(2,3,4)
addition(10,20)


