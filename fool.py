cards=input().split()
trump=input()
value={'6':1, '7':2, '8':3, '9':4, '10':5, 'J':6, 'Q':7, 'K':8, 'A':9}
if cards[0][-1]==cards[1][-1]:
    if value[cards[0][:-1]]>value[cards[1][:-1]]: print("First")
    else: print("Second")
elif cards[0][-1]!=trump and cards[1][-1]!=trump and cards[0][-1]!=cards[1][-1]: print("Error")
else:
    if cards[0][-1]==trump: print("First")
    else: print("Second")
