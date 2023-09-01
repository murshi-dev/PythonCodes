#string operations
#string concatenation - combining strings
# use + operator
first_name="John"
last_name="Doe"
print("Concatenated string is", (first_name+last_name))

#string replication
#use * operator
repeated_string="Hello" *3
print(repeated_string)

#string indexing - can access each charecter in a string
message="Hello, world!"
print(message[0])#outputs 'H'
print(message[7])#outputs 'w'

#extracting part of a string - substring
substring=message[7:12]#extract 'world' from the message
print(substring)

#finding the length of string
length=len(message)
print(length) #displays 13 counting the number of
#charecters in the message string

#string manipulation
text=" Python Programming "
print(text.strip()) #removes leading and trailing whitespaces
print(text.lower()) #to convert to lowercase letters
print(text.upper()) #to convert to uppercase letters
print(text.replace("Python","Java")) #replace python with java