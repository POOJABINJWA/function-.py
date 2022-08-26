# Q5.Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].

def funtotion(a):
    i=0
    c=[]
    while i<len(a):
        if a[i] not in (c):
            c.append(a[i])
        i=i+1
    print(c)  
funtotion([1,2,3,3,3,3,4,5])          