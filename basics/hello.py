print("hello world")

name = input("Enter your name ") #--> returns a string i.e., copied from console and assign to variable name
# print("hello, "+name) #-> concatenation
print("hello,",name) #-> ',' --> when adding multiple args to print fun it automatically adds space in between args ex:- hello, muheeb


"""
    # str is a class in python that represents string {sequence of characters}
    # every datatype in python is a class/interface
    # python is a 100% object oriented programming language
    # whereas java has types like int, double, float, char, short, byte, boolean which are not classes
      though they have wrappers to make them object
    
"""

# according to pythons documentation 
# signature of print() is
# print(*objects, sep=' ', end='\n', file=None, flush=False)

print("hello, ",end="")
print(name)

print("hello,",name,sep="--")

# "" != ''
print("hello, 'friend'") 
print("hello, \"friend\"")  # \" escape sequence using \

print(f"hello, {name}") # fstring or formatstring a special type of string

