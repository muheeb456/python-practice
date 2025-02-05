class Account:
    def __init__(self,balance):
        self._balance = balance
        
    @property
    def balance(self):
        return self._balance
    
    def __str__(self):
        return f"{self.balance} Rupees"
    
    def __add__(self,other):
        return Account(self.balance+other.balance)
    
def main():
    mark = Account(1000)
    vince = Account(5866)
    shane = Account(500)
    total = mark + vince + shane
    print(total)

if __name__ == "__main__":
    main()