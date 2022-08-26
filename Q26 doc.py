# Q26. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “FizzBuzz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

def fun():
    # a=int(input("enter the number :"))
    if a%3==0 and a%5==0:
        return("fizzbuzz")
    if a%3==0:
        return("fizz")
    if a%5==0:
        return("buzz")
    else:
        return(a)    
a=int(input("enter the number: "))
print(fun())           
            

