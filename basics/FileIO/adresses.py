import csv

def display_addresses():
    with open("./addressbook.csv") as file:
        reader = csv.DictReader(file) # iterable object
        print(f'{"NAME":15} ADDRESS')
        for row in reader: # returns a (dictionary object and key of first row first column name) for every row
            print(f'{row["name"]:15} {row["address"]}')

def add_address():
    with open("./addressbook.csv","a") as file:
        name = input("Enter name ")
        add = input("Enter address ")
        writer = csv.DictWriter(file, fieldnames=["name"])
        writer.writerow({"name":name,"address":add})
    print("added successfully")

while(True):
    add_address()
    quit = input("Add another Y/N ")
    if(quit.lower()=="n"):
        break

display_addresses()