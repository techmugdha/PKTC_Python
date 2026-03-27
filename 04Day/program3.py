student ={"name":"Tom","grades":(89,90,92,75,95)}

def avegrage(sequence):
  return sum(sequence)/len(sequence)

print(f"student: {student.get('name')}, Grades : {avegrage(student.get("grades"))}")