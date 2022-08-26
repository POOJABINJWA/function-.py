# Q39. Your task is to make two functions, max and min (maximum and minimum in PHP and Python, maxi and mini in Julia) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.
# #Examples:-

# maximun([4,6,2,1,9,63,-134,566]) returns 566
# minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
# maximun([5]) returns 5.

# minimun([42, 54, 65, 87, 0]) returns 0.


def fun():
    a=([4,6,2,1,9,63,-134,566])
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i=i+1
    print(max)
    b=[-52, 56, 30, 29, -54, 0, -110] 
    j=0
    min =b[0] 
    while j<len(b):
        if b[j] <min:
            min=b[j]
        j=j+1
    print(min)
    c=[5]
    k=0
    max=0
    while k<len(c):
        if c[k]>max:
            max=c[k]
        k=k+1
    print(max)
    d=[4,6,2,1,9,63,-134,566] 
    l=0
    min=0
    while i<len(d):
        if d[l]<min:
            min=d[l]
        i=i+1
    print(min)
fun()            




