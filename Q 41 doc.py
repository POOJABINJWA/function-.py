#Q41. Write a Python program to find the list with maximum and minimum length.
# Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])

def fun():
    a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
    i=0
    max=0
    min=1
    c=[]
    k=[0]
    while i<len(a):
        if max<len(a[i]):
            max=len(a[i])
            c=a[i]
        if min>len(a[i]):
            min=len(a[i])
            k=a[i]
        i=i+1
    print(max,c)
    print(min,k)
fun()