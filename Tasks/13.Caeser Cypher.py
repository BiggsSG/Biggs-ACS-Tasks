sentence = list(input("Enter text to be shifted: "))
shiftvalue = int(input("Enter the desired shift amount: ")) #choose how much the letters are shifted by

encrypted = "" #variable to store shifted text

for i in range(len(sentence)):
    if sentence[i]:
        ord_value = ord(sentence[i]) #converts str to ord value
        cipherValue = ord_value + shiftvalue #shifts the ord value by the shift
        if cipherValue > ord('z'):
            cipherValue = cipherValue - 26 #shifts the value back to a if it goes over the ord value for z
        #end if
        encrypted = encrypted + (chr(cipherValue)) #converts ord value back to chr
    #end if
print(encrypted)