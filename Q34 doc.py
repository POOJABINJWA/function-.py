# Q34. Write a function which converts the input string to uppercase.
# Write a function which converts the input string to uppercase.
# For example:-
# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.

def fun():
    a=[10, 14, 2, 23, 19]
    i=0
    max=0
    smax=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        elif a[i]>smax and max!=a[i]:
            smax=a[i]    
        i=i+1
    print(max,"+",smax,"=",max+smax)
fun() 
