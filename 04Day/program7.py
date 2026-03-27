# Factory Design Pattern : SOme other class/ Method produces objects of another class / Object Producing factories
FoodCaTeGORY = ('Veg', 'Non-Veg')
class Menu:
  def __init__(self,category,item,quantity):
    self.item = item
    self.quantity = quantity
    self.category = category
  
  # Class Methods: used for Factory Pattern / Object Creational Category Pattern 
  @classmethod  
  def VegMenu(cls,item, qnt):
    return cls(FoodCaTeGORY[0],item,qnt)
    # return Menu(FoodCaTeGORY[0],item,qnt)
  
  @classmethod  
  def NonVegMenu(cls,item, qnt):
    return cls(FoodCaTeGORY[1],item,qnt)
    # return Menu(FoodCaTeGORY[1],item,qnt) 
    
  def __str__(self):
    return f"Menu: {self.category}, food item: {self.item}, quantity: {self.quantity}"
 
vegorder1 = Menu.VegMenu('Veg Biryani',1) 
print(vegorder1)

nonvegorder1 = Menu.NonVegMenu('Egg Biryani',2) 
print(nonvegorder1)
  
# order1 = Menu('Veg','Veg Biryani',1)
# print(order1)
# order2 = Menu('Non-Veg','Egg Biryani',2)
# print(order2)
# order3 = Menu('Vegan','Biryani',3)
# print(order3)

