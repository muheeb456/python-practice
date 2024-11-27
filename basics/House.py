name = input("What's name ")

match name:
    case "Harry" | "Ron" | "Hermoine":
        print("Griffindor")
    # case "Ron":
    #     print("Griffindor")
    # case "Hermoine":
    #     print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:                     # catch all undefined cases
        print("Who?")