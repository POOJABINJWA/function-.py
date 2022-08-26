# Use the min function and find the minimun value of the li

# list = [8, 6, 4, 8, 4, 50, 2, 7]


# def min(a):
#     i=0
#     min=a[0]
#     while i<len(a):
#         if a[i]<min:
#             min=a[i]
#         i=i+1
#     print(min)
# min([8, 6, 4, 8, 4, 50, 2, 7])            

    

# def fun(a,b):
#     i=0
#     sum=0
#     while i<len(a):
#         sum=sum+a[i]
#         i=i+1
#     j=0
#     while j<len(b):
#         sum=sum+b[j]
#         j=j+1
#     print(sum)
# fun([1,2,3,4],[6,5,7,8,9])     


def add(a,b):
    s=0
    for  i in range(len(a)):
        s=s+a[i]
    for j in range(len(b)):
        s=s+b[j]
    print(s)
add([1,2,3,4],[6,5,7,8,9])

            

    