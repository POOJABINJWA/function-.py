# Q30. Write a function that prints all the prime numbers between 0 
# and limit where limit is a parameter.


def fun():
    a=int(input("enter the number"))
    i=1
    while i<=a:
        j=1
        c=0
        while j<i:
            if i%j==0:
               c=c+1
            j=j+1
        if c==1:
           print("prime",i)
        i=i+1
fun()               


