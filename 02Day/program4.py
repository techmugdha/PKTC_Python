# t = (1,2,3,4,5)
# print(t[2])
# t[2] = 30
# print(t)

lst = []
st = set()
t = ()
d = {} 
# print(type(lst))
# print(type(st))
# print(type(t))
# print(type(d))

tup = (5,)
# print(tup, type(tup))

# tup2 = (5,7)
tup2 = 5,7
print(tup2, type(tup2))
# destructing
n1,n2 = (6,8)
print(n1,n2, type(n1), type((6,8)))

names = "Tom, Rob"
lst_names = names.split(',')
tup_names = tuple(lst_names)
# print(tup_names, type(tup_names))
name1,name2 = tup_names
# print(f"{name1}")
# print(f"{name2}")




