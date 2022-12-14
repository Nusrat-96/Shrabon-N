text = "if you have ANY intutive idea"
print (text)

print(text.capitalize())
print (text.upper())
print(text.lower())


"""string.find(value, start, end) , it is almost similar to index but
find return -1 if value is not present and index return an excepjtion"""
print(text.find("have"))  
print(text.find("v", 2,13))      #find v between the index value 2 and 13        

print (text.index("ANY"))
print ("Is number: ", text.isalnum())
print ("Is alphabet:", text.isalpha())          #The isalpha() method returns True if all the characters are alphabet letters (a-z).
print ("Is Ascii:", text.isascii())
print ("Is decimal:", text.isdecimal())
print ("Is digit:", text.isdigit())
print ("Is numeric: ", text.isnumeric())
print ("Is lower: ", text.islower())
print ("Is space :", text.isspace())
print ("Is Title:", text.istitle())
print("Replace : ", text.replace("i", "It"))
print ("Split: ",text.split())              #Convert the string to list 
print ("Title:", text.title())
print ("line Split:", text.splitlines())