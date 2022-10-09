n = int(input("enter the number of the students:"))
res = []
grade = []
for i in range(n):
    name = input()
    marks = float(input())
    res.append([name,marks])
    grade.append(marks)
#print(res)
#print(grade)
# duplicate plus acending order
grade = sorted(set(grade))
#print(grade)
m = grade[1]
#print(m)
name=[]
#print(name)
for val in res:
    if m==val[1]:
        name.append(val[0])
# print(name)
name.sort()
for nm in name:
    print(nm)
