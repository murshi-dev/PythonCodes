#Write code to create a file, write some contents to it.

with open("sample.txt",'w') as file:
    file.write("Sample text entered in the text file")

# Read the contents from the file and display in the console.

with open("sample.txt",'r') as file:
    content=file.read()

print(content)

#append some more text to the file
with open("sample.txt",'a') as file:
    file.write("new text appended to the text file")
    # Read the contents from the file and display in the console.

with open("sample.txt", 'r') as file:
    content = file.read()

print(content)