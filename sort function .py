# Using sort function sort the given list.

# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 


# def add(a):
#     i=0
#     while i<len(a):
#         a.sort()
#         i=i+1
#     print(a)
# add([6, 8, 4, 3, 9, 56, 0, 34, ])

def add(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    print(a)
add([6, 8, 4, 3, 9, 56, 0, 34, ])                


