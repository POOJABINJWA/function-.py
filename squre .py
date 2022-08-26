
# Q9.Write a Python program to generate and print a list of first and 
# last 5 elements where 
#   the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

def fun():
    i=0
    b=[]
    c=[]
    d=[]
    while i<=30:
        if i>=1 and i<=5:
            b.append(i*i)
        elif i>=25 and i<=30:
            c.append(i*i)
        i=i+1
    d.append(b)
    d.append(c)
    print(d)
fun()                


# def fun():
#     i=0
#     a=[]
#     b=[]
#     c=[]
#     while i<=30:
#         if i>0 and i<=5:
#             a.append(i*i)
#         elif i>25 and i<=30:
#             b.append(i*i)
#         i=i+1
#     c.append(a)
#     c.append(b)
#     print(c)
# fun()
        