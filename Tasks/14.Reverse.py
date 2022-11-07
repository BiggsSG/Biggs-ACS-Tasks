def reverser(x): # function created to reverse text 
 return x[::-1] # creates a slice which moves back through the string

reversetext = reverser(input("Enter your word to reverse: ")) # funtion used on input to reverse text
print(reversetext) # prints text 