# Q17. Write a function to tell user if he/she is able to vote or not.
# ( Consider minimum age of voting to be 18. )

def vote():
    a=int(input("enter the number:"))
    if a>=18:
        print(" he/she can do vote")
    else:
        print("they can't vote")
vote()