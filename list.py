# n = int(input("enter thr number of commands :")) 
# lst = [] 
# for i in range(n): 
#     cmd = input().split() 
#     if cmd[0] == 'insert':
#         lst.insert(int(cmd[1],cmd[2])) 
#     elif cmd[0] == 'remove':
#         lst.remove(int(cmd[1]))
#     elif cmd[0] == 'append':
#         lst.append(int(cmd[1]))
#     elif cmd[0] == 'sort':
#         lst.sort()
#     elif cmd[0] == 'pop':
#         lst.pop()
#     elif cmd[0] == 'print':
#         print(lst)
#     else:
#         lst.reverse()


# #we asked user for and input

# lst = []
# n = int(input("enter number : ")) 
# for i in range(n): 
#     cmd = input().split() 
#     if cmd [0] == 'insert':
#         lst.insert(int(cmd[1],cmd[2]))
#     elif cmd[0] == 'print':
#         print(lst)      
#     elif cmd [0] == 'remove':
#         lst.remove(int(cmd[1]))
#     elif cmd [0] == 'append':
#         lst.append(int(cmd[1]))
#     elif cmd [0] == 'sort':
#         lst.sort()
#     elif cmd [0] == 'pop':
#         lst.pop()
#     else:
#         lst.reverse()

if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(0,N):
        cmd=input().split()
        if cmd[0] == "insert":
            L.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
            L.append(int(cmd[1]))
        elif cmd[0] == "pop":
            L.pop()
        elif cmd[0] == "print":
            print(L)
        elif cmd[0] == "remove":
            L.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            L.sort()
        else:
            L.reverse();