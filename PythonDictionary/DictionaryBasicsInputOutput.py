#create empty dictionary
user_dictionary={}
#use loop to get input
while True:
    key=input("Enter the key: ('quit' to exit)")
    if(key=='quit'):
        break
    value = input("Enter the value:")
    #add key and value to user_dictionary
    user_dictionary[key]=value
#use loop to display dictionary
#use items() to display key value pair
for key,value in user_dictionary.items():
        print(f'{key}:{value}')

#display only key - keys()
for key in user_dictionary.keys():
    print(key)

# display only values - values()
for value in user_dictionary.values():
    print(value)