# def swap_case(s):
#     x=''
#     for c in s:
#         if c.isupper():
#             c = c.lower()
#         else:
#             c = c.upper()
#     x+=''.join(c)

#     return x
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

def swap_case(s):
    result = []
    for letter in s:
        if letter == letter.lower():
            result.append(letter.upper())
        elif letter == letter.upper():
            result.append(letter.lower())
        else:
            result.append(letter)
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
