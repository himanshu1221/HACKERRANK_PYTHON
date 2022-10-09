n = int(input())
s = set(map(int, input().split()))
cmd = int(input())
for i in range(cmd):
    s1=list(input().split())
    if s[0]=='pop':
        s.pop()
    elif s[0]=='remove':
        s.remove(int(s1[1]))
    elif s[0]=='discard':
        s.discard(int(s1[1]))
sum=0
for i in s:
    sum=sum+1
print(sum)


# the code

num = int(input())
data = set(map(int, input().split()))
operations = int(input())

for x in range(operations):
  oper = input().split()
  if oper[0] == "remove":
    data.remove(int(oper[1]))
  elif oper[0] == "discard":
    data.discard(int(oper[1]))
  else:
    data.pop()
    
print(sum(data))

            
