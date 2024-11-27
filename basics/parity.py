def main():    
    x = int(input("What's x "))
    if is_even(x):
        print("even")
    else:
        print("Odd")

def is_even(n):
    # return True if n%2 == 0 else False
    return n % 2 == 0       # returns bool either "True" or "False"
main()