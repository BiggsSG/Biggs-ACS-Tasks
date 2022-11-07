Number = int(input("Please input a number between 100-999 "))
Hundreds = Number // 100
Tens = (Number % 100) // 10
Units = (Number % 10)
print (str(Hundreds) + " hundreds " + str(Tens) + " tens "  + str(Units) + " units")