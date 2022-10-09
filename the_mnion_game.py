# def minion_game(string):
#     # your code goes here
#     s1=0
#     s2=0
#     vow='AEIOU'
#     for i in range(len(string)):
#         if s[i] not in vow :
#             len(string[i:])
#         else:
#             s2=s+len(string[i:])
#     if s1>s2:
#         print("Stuart",s1)
#     elif s2>s1 :
#         print("Kevin",s1)
#     else:
#         print("Draw")
 
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


def minion_game(string):
    # your code goes here
    player1 = 0;
    player2 = 0;
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            player1 += (str_len)-i
        else :
            player2 += (str_len)-i
    
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)