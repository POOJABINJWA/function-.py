#  By using reverse function print the reverse order of the 

# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]


def reverse(a):
    i=0
    # rev=1
    while i<len(a):
        a.reverse()
        i=i+1
    print(a)

reverse(["Z", "A", "A", "B", "E", "M", "A", "R", "D"])       

