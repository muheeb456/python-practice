import re

name = input("What's your name? ").strip()
if matches := re.search(r"^([a-zA-Z]*),? *([a-zA-Z]*)$",name): # := walrus operator
    name = matches.group(1)+" "+matches.group(2)
    print(f'hello, {name}')
else:
    print("This is not a proper name, be sure to provide a full name")