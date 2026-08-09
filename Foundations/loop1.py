'''#
# num = ['1','2','3']
 #for num in num:
 #   print(f"i am eating {num}") '''
def funct(n):
    if (n==0 or n==1):
     return 1
    else:
       return n * funct(n-1)

 
fact=int(input(" kati ko fact chaiyoo"))
answer=funct(fact)
print(answer)