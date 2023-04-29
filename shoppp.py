# Question 1 - 

# Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 

# Book - Introduction to Python Programming : Rs 499.00

# Book - Python Libraries Cookbook : Rs. 855.00

# Book - Data Science in Python : Rs. 645.00


# Taxes and additional charges are described as details - 

# GST : 12%

# Delivery Charges : Rs. 250.00





#solution






print('''List of avialable books are given below\nIntroduction to Python Programming : Rs 499.00\nPython Libraries Cookbook : Rs. 855.00\nSelect 3 for Data Science in Python : Rs. 645.00\ngive input 0 if you don't want that book to purchase''')

def library():                                                                #for taking the user inputs
    a=int(input("enter no.of Introduction to Python Programming = "))
    b=int(input("enter no.of Python Libraries Cookbook costs = "))
    c=int(input("enter no.of  Data Science in Python costs = "))
    return a*499.00+b*855+c*645

total=library()





def delivery_charges(total):                                                        #checking for the total if the user give all the inputs as 0's then ask another time to purchase 
    if total==0:
        a=int(input("do you want purchase any book\n for YES click 1 \n for NO click 0"))
        if a==0:
            return 0
        if a==1:
            print("To purchase any Books give valid inputs ")
            total=library()
    else:
        return 250
    return 250

including_gst=1.12*total+delivery_charges(total)                #calculating the total amount including gst and delivery charges
i=including_gst
print("Amount only for Books total = {0}".format(total))
print("Amount for delivery charges = 250.00")
print("12% GST")
print("total+12% GST+Rs.250.00 Delivery Charges=",i)








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





