# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12


def fun(a):
    d=a.split()
    i=0
    count1_upper=0
    count_lower=0
    while i<len(d):
        j=0
        while j<len(d[i]):
            if d[i][j]==d[i][j].upper():
                count1_upper=count1_upper+1
            elif d[i][j]==d[i][j].lower():
                count_lower=count_lower+1 
            j=j+1
        i=i+1
    print("upper case",count1_upper)
    print("lower case",count_lower) 
a=input("enter the word :")
fun(a)                  
