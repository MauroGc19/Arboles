def MinDiv(n,i):
    if i==0:
        return n
    else:
        return MinDiv(i,n%i)
def MinDiv_iterativo(n,i):
    if i==0:
        return n
    else:
        a=0
        for a in range(1,5):
            c=n%i
            n=i
            i=c 
            if c==0:
                a=4
        return c  
print(MinDiv_iterativo(48,18)) 