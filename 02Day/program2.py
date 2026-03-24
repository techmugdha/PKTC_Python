def greet(name,message=''):
  print(f'Hello {name} , you got a message = {message}')
  
# greet('Hugh Jackman', 'I loved that film!')
# greet('Hugh Jackman')

def greet_players(name, names= None):
  if names is None:
    names  = []
  names.append(name)
  for nm in names:
    print(f"Hello, {nm}")
  
greet_players('Ronaldo')
greet_players('Virat')
greet_players('Messi')


  