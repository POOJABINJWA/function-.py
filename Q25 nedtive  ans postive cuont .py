# Q25. Given a list of numbers, write a Python program to count positive 
# and negative numbers in a List using function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

def fun():
    a=[2, -7, 5, -64, -14]
    i=0
    c=0
    c1=0
    while i<len(a):
        if a[i]>0:
            c=c+1
        else:
            c1=c1+1
        i=i+1
    print("postivie number",c)
    print("nagative number",c1)
fun()    
