# Q42. Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
# The original list is : [15, 81, 11, 234]


def fun(a):
    # a=[12, 67, 98, 34]
    i=0
    b=[]
    while i<len(a):
        d=a[i]%10
        c=a[i]//10
        n=d+c
        b.append(n)
        i=i+1
    print(b)
fun([12, 67, 98, 34])        
