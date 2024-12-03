def main():
    n = get_number()
    sayMeow(n)

def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0 :
            return n

def sayMeow(n):
    for _ in range(n):  #just for better readability
        print("meow")

# for i in [0,1,2]:
#     print("meow")

# for i in range(3):
#     print("meow")

# while True:
#     n = int(input("what's n? "))
#     if n > 0 :
#        break

# for _ in range(3):
#     print("meow")

# print("meow\n"*3,end="")



# for _ in range(n):
#     print("meow")

main()

