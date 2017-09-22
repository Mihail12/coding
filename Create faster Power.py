def power(a,n):
    if a==0 and n==0: return 0
    if n<0: return power(1/a,-n)
    if n==0: return 1
    if n==1: return a
    if n%2==1: return a*power(a*a,(n-1)//2)
    else: return power(a*a,n//2)
print( power( float(input()) , int(input()) ) )
