def merge_the_tools(string, k):
    l=[]
    z=0
    for i in range(len(string)//k):
        l.append(string[z:z+k])
        z+=k  
        print(l)
        for v in  l:
            print(list(v))
            print(dict,fromkeys(list(v)))
            print(dict,fromkeys(list(v),1))
            print(dict,fromkeys(list(v)).keys())
            print(list(dict,fromkeys(list(v)).keys()))
            print(' '.join( list(dict,fromkeys(list(v)))))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)