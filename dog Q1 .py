
# Q1.Write a Python program to count the number of strings where the string length is 2   
#   or more and the first and last characters are the same from a given list of strings.
#  ist=['abc', 'xyz', 'aba', '1221']
# result= 2.


def list(a):
    i=0
    c=0
    while i<len(a) :
        if a[i][0]==a[i][-1]:
            c=c+1
        i=i+1
    print(c)    
list(['abc', 'xyz', 'aba', '1221'])           

# def fun():
#     list=['abc', 'xyz', 'aba', '1221']
#     i=0
#     c=0
#     while i<len(list):
#         if list[i][0]==list[i][-1]:
#             c=c+1
#         i=i+1
#     print(c)
# fun()