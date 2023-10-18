class atm():
    def __init__(self,name,atmCardNO,pinCardNo,balance):
        self.atmCardNo= atmCardNO
        self.pinCardNo=pinCardNo
        self.name=name
        self.balance=balance

    def cashWithdrawl(self,amount):
        self.balance=self.balance-amount
        print('cashWithdrawl',amount,'remaining balance is:',self.balance)

    def balanceEnquiry(self):
        print("your balance is ",self.balance)

card_no=input('Enter your card number:')
pin_no=input('Enter you pin: ')
new_user=atm('Joe',card_no,pin_no,50000)
new_user.balanceEnquiry()
new_user.cashWithdrawl()

        