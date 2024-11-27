def main():
    name = input("What is your name ")
    sayHello()
    sayHello(name)  #name is an argument passed to sayHello method

def sayHello(to="World"): #to is default valued parameter
    print("Hello,",to)

main()

'''
    functions need to defined before they are called in python.
    call the main method always at the end to prevent NameErrors.
    variables are scoped in their respective function and cannot be accessed in other functions.
'''