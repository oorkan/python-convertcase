message = input("Please write the string you want to case-convert: ")
option = input("Please choose from the following options: \n \
  L for lower case \n \
  U for upper case \n \
  T for title case \n \
  C for capitalized case \n \
  S for swap case \n \
  ______________________________ \n \
\n \
  > ")

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

print("\n" + message)
