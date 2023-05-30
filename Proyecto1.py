
def recursive_cronometro(n):
    if n==0:
        return n
    else:
        print(n)
        return recursive_cronometro(n-1)
print(recursive_cronometro(5))  
def power(n,i):
    if i==1:
        return n
    else:
        return n*power(n,i-1)
print(power(2,52))    