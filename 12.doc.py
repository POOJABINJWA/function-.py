# Q12.Numbers ending with zeros are boring.

# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

# def fun():
#     a=[1450,96000,1050,-1050]
#     d=str(a)
#     i=0
#     b=[]
#     while i<len(a):
#         if type(d[i])==list:
#            j=0
#            while j<len(a[i]):
#                 if d[i][j]!="0":
#                     b.append(a[i][j])
#                 j=j+1
#         else:
#             b.append(a[i])        
#         i=i+1
#     print(b)
# fun()    



def fun(a):
    # a=[1450,96000,1050,-1050]
    i=0
    b=[]
    d=str(a)
    while i<len(a):
        while a[i]>0 or a[i]<0:
            if a[i]%10!=0:
                b.append(a[i])
                break
            a[i]//=10
        i=i+1
    print(b)
fun([1450,96000,1050,-1050])


# def fun():
#     a=[1450,96000,1050,-1050]
#     i=0
#     b=[]
#     d=str(a)
#     while i<len(a):
#         while a[i]>0:
#             if a[i]%10!=0:
#                 b.append(a[i])
#                 break
#             a[i]//=10
#         i=i+1
#     print(b)
# fun()



        