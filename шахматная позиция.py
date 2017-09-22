#My
n,m=tuple(map(int,input().split()))
k,l=[1,1]
for i in range(n):
    if i%2==1 and i>0 and (m%2==0 or n%2==0): l=0
    
    for j in range(m):
        if l:
            print('{:>4}'.format(k),end='')
            k+=1
            l=0
        else:
            print('{:>4}'.format(0),end='')
            l=1
    if i%2==1 and i>0 and (m%2==0 or n%2==0): l=1
    print()

# solution 1
n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]
counter = 1
for i in range(n):
    for j in range(i%2, m, 2):
        matrix[i][j] = counter
        counter += 1
for x in matrix:
    print("".join(["{:>4}".format(y) for y in x]))

# solution 2

n,m=[int(i) for i in input().split()]
x=0
lst={}

for i in range(n):
    for j in range(m):
        if (i+j)%2==0:
            x+=1
            lst[(i,j)]=x
        else:
            lst[(i,j)]=0
for i in range(n):
    for j in range(m):
        print('{0:>4}'.format(lst[(i,j)]),end='')


# solution 3
n, m = map(int, input().split())
print("\n".join(["".join(["{:>4}".format([(j*m+i+2)//2, 0][(i+j) % 2]) for i in range(m)]) for j in range(n)]))
