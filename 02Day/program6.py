# packing of argument : *args
lst  = [1,2,3,4,5]
first,*rest = lst
print(first) #1
print(rest) # [2,3,4,5]
*rest, last = lst
print(rest) # [1,2,3,4]
print(last) # 5