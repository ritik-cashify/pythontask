#def adder(x,y,z):
    #print("sum:",x+y+z)

#adder(5,10,15,20,25)
#This function will show error when we try to run this
#Solution is args

def addfn(*number):
    s = 0

    for n in number:
        s = s + n

    print("Sum is",s)

addfn(4,5,6,7)
addfn(1,2,3,5,6)