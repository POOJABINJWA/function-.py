# Q44.Bonus - Given the same list, print the last ‘N’ elements in reverse order.
# Sample Input:
# 2
# Sample Output:
# q
# b 
# Sample Input:
# 3
# Sample Output:
# q
# b 
# 5

def fun():
   n=int(input("enter thr number"))
   a=["a",1,"2",5 ,"b","q"]
   i=0
   while i<len(a):
        i=i+1
   print(a[-1:-n:-1])
fun()    
