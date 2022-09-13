Number = int(input("Please enter a number "))
Divisor = int(input("Please enter a divisor "))
Total = int(Number/Divisor) # converted to int so no decimal is formed 
Remainder = Number % Divisor
print (str(Total) + " remainder " + str(Remainder)) # converted back to string for concatination 