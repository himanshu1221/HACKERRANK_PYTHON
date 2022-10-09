# if __name__ == '__main__':
#     s = input()
#     if s.isalnum():
#         print("True")
#     else:
#        print("False")
#     if s.isalpha():
#         print("True")
#     else:
#         print("False")
#     if s.isdigit():
#         print("True")
#     else:
#         print("False")
#     if s.islower():
#         print("True")    
#     else:
#         print("False")    
#     if s.isupper():
#         print("True")
#     else:
#         print("False")

if __name__ == '__main__':
    s = input()
    print(any(a.isalnum() for a in s) )
    print(any(a.isalpha() for a in s) )
    print(any(a.isdigit() for a in s) )
    print(any(a.islower() for a in s) )
    print(any(a.isupper() for a in s) )