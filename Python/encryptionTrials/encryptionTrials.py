print("NOTE : AVOID USING SIGNS LIKE '!#\"' for successful decryption")


def convertSpacesToDashes(string):
    finalString = ""
    for i in string:
        if (i==' '):
            finalString += '_'
            
        else:
            finalString += i
    return finalString

def convertDashesToSpaces(string):
    finalString = ""
    for i in string:
        if (i=='_' or i=='-'):
            finalString += ' '
        else:
            finalString += i
            
    return finalString
    

def encryptThis(string):
    string = convertSpacesToDashes(string)
    encryptedString =""
    counter = 1
    reverse = False
    for i in string:
            if (counter > 5):
                counter = 1
            if reverse:
                encryptedString += chr(ord(i) - counter)
            else:
                encryptedString += chr(ord(i) + counter)
            counter += 1
            reverse = not reverse
            
    return encryptedString
            
def decryptThis(string):
    
    encryptedString = ""
    counter = 1
    reverse = True
    for i in string:
        if (counter > 5):
            counter = 1
        if reverse:
            encryptedString += chr(ord(i) - counter)
        else:
            encryptedString += chr(ord(i) + counter)
        counter += 1
        reverse = not reverse
        
    return convertDashesToSpaces(encryptedString)
    

            
    





print("Enter whether you want to decrypt or encrypt:")
print("1. Encrypt")
print("2. Decrypt")
userInput = int(input("Enter the number : "))

if (userInput ==1):

    stringToConvert = input("Enter the string : ")
    print("The string to encrypt is : ")
    print("'" + encryptThis(stringToConvert) +  "'")
    
    

elif (userInput == 2):
    stringToConvert = input("Enter the string : ")
    print("The decrypted string is : ")
    print( "'" + decryptThis(stringToConvert) + "'")
    

    

else:
    print("Invalid!!")








