def get_number(prompt):
    while True:
        try:
            '''x = int(input("What's x? "))
            return x'''
            return int(input(prompt))
        except ValueError:
            print(f"x is not a integer")
        '''else:
            return x'''
    '''
        when error gets raised x is not defined on line 4
    '''
        
def main():
    '''print(f'x is {get_number()}')'''
    x = get_number("What is x? ")

if __name__ == "__main__":
    main()