# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].

def even(a):
    i=0
    c=[]
    while i<len(a):
        if a[i]%2==0:
            c.append(a[i])
        i=i+1
    print(c)                
even([1, 2, 3, 4, 5, 6, 7, 8, 9])    

            