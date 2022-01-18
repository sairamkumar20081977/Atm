class Atm :
    def __init__(self,cardNumber,pin) :
        self.cardNumber=cardNumber
        self.pin=pin
    def check_balance(self):
        print("your balance is 10000")
def main():
    card_number=input("insert your card number")
    pin_number=input("enter your pin number")
    new_user=Atm(card_number,pin_number)
    new_user.check_balance()
if __name__=="__main__":
    main()
 
    