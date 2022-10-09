# num = []
# z=num.append(int(input("enter the list number: ")))
# print(num)
# a=[]

# x = a.append(int(input("enter the number in set a:")))
# b=[]
# y = b.append(int(input("enter the number in set a:")))
m,n=map(input().split())
array= list(map(int(input().split())))
a = set(map(int(input().split)))
b = set(map(int(input().split)))
print(sum((i in a)-(i in b) for i in array))

