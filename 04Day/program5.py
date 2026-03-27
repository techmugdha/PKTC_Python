class Emp:
  # class variable / Properties
  company_name = 'BVS'
  
  def __init__(self,name,dept):
    # print("first __init__")
    # Instance variable
    self.name = name
    self.dept = dept
    
Emp.company_name = "Zensar"  
     
e1 = Emp('Hugh Jackman','IT')
# e1.name = "Samwise Gamgee"
# e1.company_name = "Zensar"
# print(e1.__dict__)
print(e1.company_name) # Zensar

e2 = Emp('Rob',"HR")
print(e2.company_name) # BVS

# print(e2.__dict__)
# print(Emp.company_name)


