# Question 1 - 

# Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 

# Book - Introduction to Python Programming : Rs 499.00

# Book - Python Libraries Cookbook : Rs. 855.00

# Book - Data Science in Python : Rs. 645.00


# Taxes and additional charges are described as details - 

# GST : 12%

# Delivery Charges : Rs. 250.00





#solution

import sys


print('''List of avialable books are given below\nIntroduction to Python Programming : Rs 499.00\nPython Libraries Cookbook : Rs. 855.00\nSelect 3 for Data Science in Python : Rs. 645.00\ngive input 0 if you don't want that book to purchase''')

def library():
    try:
        a=int(input("enter no.of Introduction to Python Programming = "))
    except:
        print("invalid input")
        return 0
    try:
        b=int(input("enter no.of Python Libraries Cookbook costs = "))
    except:
        print("invalid input")
        return 0
    try:
        c=int(input("enter no.of  Data Science in Python costs = "))
    except:
        print("invalid input")
        return 0
    

    if a&b&c==0:
        deli=0
    else:
        deli=250

    total=1.12*(a*499.00+b*855+c*645)+deli
    # return a*499.00+b*855+c*645
    return total


total=library()


def user_interaction(total):
    if total==0:
        try:
            a=int(input("do you want purchase any book\n for YES click 1 \n for NO click 0\n"))
        except:
            print("invalid input")
            return 0
        if a==0:
            print("thanks for visiting")
            sys.exit(0)                        # to terminate the program
        if a==1:
            print("To purchase any Books give valid inputs ")
            total=library()
    else:
        return 250
    return total

including_gst=total
z=0
while(z==0):                           #checking if the total is > 0 print result and stop the program , if not ask the user to purchase the books are not.
    if including_gst>0:
        print("total+12% GST+Rs.250.00 Delivery Charges=",including_gst)
        print("happy learning")
        z=1
    else:
        including_gst=user_interaction(total)   #user interaction







# Question 2 - 

# Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.

                                  

# Input : string1 = "India"

# Output : uniqueLetters = i,n,d,a


# Input : string1 = "Dedication"

# Output : uniqueLetters = d,e,i,c,a,t,o,n

# solution

a=input('string1 = ')                 # taking the input
b=set(a)                              # forming a set from user input
print( 'uniqueLetters = ',end= '')    
print(*b, sep = ',')                  #printing the required output





