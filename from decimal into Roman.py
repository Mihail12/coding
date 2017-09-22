di={1:'I',
    4:'IV',
    5:'V',
    9:'IX',
    10:'X',
    40:'XL',
    50:'L',
    90:'XC',
    100:'C',
    400:'CD',
    500:'D',
    900:'CM',
    1000:'M'}
n=str(input())
out=''
for i in range(len(n)):
    n1=int(n[i])
    f=n1*10**(len(n)-(i+1))
    if n1==0: continue
    elif f in di:
        out+=di[f]
    else:
        if int(n[i])<4:
            out+=di[f//n1]*n1
        else:
            out+=di[5*10**(len(n)-(i+1))]+di[f//n1]*(n1-5)
print(out)
    
    

    
