print ("Please input a number from 1-3")
Choice = int(input())
while Choice not in [1,2,3]: # validation for num between 1-3
    Choice = int(input("Please input a number from 1-3 "))  
else:
    print ("You have selected option number " + str(Choice)) # converted back to string for concatination 
# end while