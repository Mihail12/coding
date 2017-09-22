def find(seq,row,col):
    lis=[(1,0),(-1,0),(0,1),(0,-1)]
    for var in lis:
        boolean= row+var[0]>=0 and row+var[0]<len(seq) and col+var[1]>=0 and col+var[1]<len(seq)
        if  boolean and seq[row+var[0]][col+var[1]]==1:
            seq[row+var[0]][col+var[1]]=2
            find(seq,row+var[0],col+var[1])
        


def amount_of_lakes(seq):
    n=0
    for row in range(len(seq)):
        for col in range(len(seq[row])):
            if seq[row][col]==1:
                seq[row][col]=2
                find(seq,row=row,col=col)
                n+=1
                for i in seq:
                    print(*i)
                print()
    return n
