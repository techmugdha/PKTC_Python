def demo():
  id = input("Enter id: ")
  name = input("Enter name: ")
  city = input("Enter city: ")
  return id,name,city

info = demo()
print(info,type(info))

# Destructing tuple
_,nm,city = demo()
print(f"Hello {nm}, you are from {city}")