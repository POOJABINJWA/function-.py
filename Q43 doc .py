# Q43.  Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last ‘N’ elements 
# of the given list. ‘N’ is accepted from the user.
# Sample Input:
# 1
# Sample Output:
# q 
# Sample Input:
# 3
# Sample Output:
# 5"
# b 

def add():
   n=int(input("enter thr number"))
   a=["a",1,"2",5 ,"b","q"]
   i=0
   while i<len(a):
        i=i+1
   print(a[-n:]) 
add()       

