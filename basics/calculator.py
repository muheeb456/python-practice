x = float(input("Enter number a "))
y = float(input("Enter number b "))

# + works as concatenation for strings and addition for numbers
# round function takes one optional argument which is num to specify "max decimal digits". 
z = round(x+y,2)

# automatically add comma for every three digits using f string
print(f"x + y = {z:,}")

z = x/y
# exactly does same as round function
print(f"x/y = {z:.2f}")