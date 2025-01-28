import sys

def readName():
    
#check for errors
    if len(sys.argv) < 2:
        sys.exit("pass yor name as argument")

    elif len(sys.argv) >2:
        sys.exit("need only one argument i.e., your name")

    print("Hello, my name is",sys.argv[1])

def readNames():

    if len(sys.argv) < 2:
        sys.exit("pass yor name as argument")
    for name in sys.argv[1:]:
        print("Hello, my name is",name)

readNames()

def main():
    readNames()

if __name__ == "__main__":
    main()