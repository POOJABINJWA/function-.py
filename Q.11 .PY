# Q11.Implement a function named generateRange(min, max, step), which takes three arguments and 
# generates a range of integers from min to max, with the step. 
# The first integer is the minimum value, the second is the maximum of the 
# range and the third is the step. (min < max)

# Task
# Implement a function named

# generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
# generate_range(1, 10, 3) # should return list of [1,4,7,10]
# generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
# generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]
# Note
# min < max
# step > 0
# the range does not HAVE to include max (depending on the step)


def fun():
    i=2
    b=[]
    while i<=10:
        b.append(i)
        i=i+2
    # print(b)
# fun()

# def fun():
    # i=1
    c=[]
    while i<=10:
        c.append(b)
        i=i+3
    print(c )
fun()        

