name = input("Enter your name ")

# return the given string without any whitespaces on either sides
# name = name.strip()

# capitalize the first letter in the first word
# name = name.capitalize()

# remove whitespaces and capitalize user's name
name = name.strip().title()

# print(f"hello, {name}")

firstName , lastName = name.split(' ')

print(f"hello, {firstName}")
