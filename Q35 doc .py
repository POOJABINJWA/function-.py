# Q35. Kids drink toddy.
#     Teens drink coke.
#     Young adults drink beer.
#     Adults drink whisky.
#     Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky".


def fun(a):
    # a=int(input("enter the number :"))
    if a<14:
        print("toddy")
    elif a<=18:
        print("cock")
    elif a>=21:
        print("whisky")  
fun(12)
fun(17)  
fun(35)         
