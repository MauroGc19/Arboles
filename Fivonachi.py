def fivonachi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
         return fivonachi(n-1)+fivonachi(n-2)        
            
print(fivonachi(3))
 