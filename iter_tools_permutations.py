from itertools import permutations
a=input().split()
s = sorted(a[0])
num = int(a[1])
print(*list(map(''.join,permutations(a,num))),space='\n')


# solution 
from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')