x = int(input("Whats x "))
y = int(input("Whats y "))

if x > y:
    print("x is greater than y")

if x < y:
    print("y is greater than x")

if x == y:
    print("x is equal to y")

""" The above code check all the conditions every time . Hence to improve we can use elif and else"""

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

""" The above code is more efficient since any condition is the other conditions wont check"""

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

""" When all the if and elif conditions are false else will execute"""

if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")

""" or is logical operator which return true if any one of the condition is true """

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")