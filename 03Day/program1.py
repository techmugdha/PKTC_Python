lst = [1,2,3,4,5,6,7,8,9,10]
double = []
for nm in lst:
  if nm == 6:
    break
  double.append(nm*2)
  # print(nm * 2)

# print(double)

# List comprehension syntax
double_lst = [nm*2 for nm in lst if nm < 6]
print(double_lst)