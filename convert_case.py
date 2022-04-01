message = str(input("Please write the string you want to case-convert: "))
option = str(input("Please choose from the following options: \n \
  L for lower case \n \
  U for upper case \n \
  T for title case \n \
  C for capitalized case \n \
  S for swap case \n \
  A for alternate case \n \
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

if option.lower() == "a":
    message_lower = message.lower()
    counter = 0
    charlist = []

    for char in message_lower:
        counter = -1 if char == " " else counter

        if (counter % 2 != 0):
            charlist.append(char.upper())
        else:
            charlist.append(char)

        counter += 1

    message = ''.join(charlist)
    
print("\n" + message)