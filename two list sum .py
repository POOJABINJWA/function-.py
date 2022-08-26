# Write a function named add_numbers_list which takes 2 lists of two integers 
# and then prints the sum of the integers with the same position.

# Use the add_numbers function given in Part 1 to count 2 integers that have
#  the same position.

# If we give [50, 60, 10] and [10, 20, 13] to this function it will print this

# def add(num1,num2):
#     print(num1+num2)
# add(56,12)  
# 
# def sum(list):
#     i=0
#     sum=0
#     while i<len(list):
#         if type(list[i])==list:
#             sum=sum+(list[i])+(list[i])
#         i=i+1
#     print(sum)
# sum([[50, 60, 10],[10, 20, 13]])          
def function(a,b):
    i=0
    d=[]
    while i<len(a):
        c=a[i]+b[i]
        d.append(c)
        i=i+1
    print(d)
function([50,60,10],[10,20,13])