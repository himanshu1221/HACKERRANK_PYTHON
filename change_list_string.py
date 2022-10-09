# string= list(input("enter the string: "))
# lst = []
# index = int(input("enter the index:"))
# chng_index = [index]
# rep_word = input("enter the word you want to replace :")
# for letter in string:
#     lst.append(letter)
# print(lst)
# key = lst[index]
# string[key]=index[lst]
# print(string)

def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)