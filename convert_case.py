message = str(input("Please write the string you want to case-convert: "))
option = str(input("Please choose from the following options: \n \
  L for lower case \n \
  U for upper case \n \
  T for title case \n \
  C for capitalized case \n \
  S for swap case \n \
  OU for upper case by even ordering \n \
______________________________ \n \
\n \
  > "))

if option.lower() == "l":
	message = message.lower()

if option.lower() == "u":
	message = message.upper()

if option.lower() == "t":
	message = message.title()

if option.lower() == "c":
	message = message.capitalize()

if option.lower() == "s":
	message = message.swapcase()

if option.lower() == "ou":
    order = 0
    counter = 0
    listO = []
    for each in message:
        if each == " ":
            counter=0            
        if(counter % 2 == 0):
            listO.append(each.upper())
        else:
            if each != " " and message[order] == each.upper():
                listO.append(message[order].lower())              
            else:
                listO.append(message[order])
                               
        order+=1
        counter+=1
    message = ''.join(listO)
    
print("\n" + message)