number = int(input("Please enter a number "))
for i in range(1, number + 1):
    if number%i == 0: # checks number is a whole integer
        print (number//i)

