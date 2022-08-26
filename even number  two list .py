# o check this, use the check_numbers function written in the previous Part 1.

# If you call your function [2, 6, 18, 10, 3, 75] and [6, 19, 24, 12, 3, 87] then it should give 
# this output:



def even(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and  b[i]%2==0:
            print("both are even")
        else:
            print("both are not even")
        i=i+1
even([2,6,18,10,3,75],[6,19,24,12,3,87])


# def funtotion(a,b):
#     for i in range(0,len(a)):
#         for j in range(0,len(b)):
#             if i==j:
#                 if a[i]%2==0 and b[j]%2==0:
#                     print("both are even")
#                 else:
#                     print("both are not even")

# funtotion([2, 6, 18, 10, 3, 75] ,[6, 19, 24, 12, 3, 87])   