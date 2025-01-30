def main():
    with open("names.txt","a") as file:
        name = input("Enter name ")
        file.write(f"{name}\n")
    readNamesSorted()

def readNamesSorted():
    names=[]
    with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip())
    for name in sorted(names):
        print(f'hello, {name.capitalize()}')


if __name__=="__main__":
    main() 