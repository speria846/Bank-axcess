
from datetime import datetime


class Account:
    def __init__(self,name,number):
            self.name=name
            self.number=number
            self.loon=0
            self.balance=0
            self.statement=[]
    def show_balance(self):
        return "your balance is {self.balance}"
    def deposit(self,amount):
        if amount<=0:
            return "deposit a valid amount"
        else:  
            self.balance += amount
            now=datetime.now()
            transuction={
            "amount":amount,
            "balance":self.balance,
            "naration":"You deposited",
            "time":datetime.now()
             }
            self.statement.append(transuction)
            return self.show_balance()
    def show_statement(self):
        for transuction in self.statement:
            amount=transuction["amount"]
            narration=transuction["narration"]
            balance=transuction["balance"]
            time=transuction["time"]
            date=transuction["date"]
            print (f"{amount}....{date}.... {narration}.... {amount}....balance {balance}.")

 


    def withdraw(self,amount):
        totalwithdraw=amount+self.transaction

        if amount<=0:
                return "the valid amount"
        elif totalwithdraw>self.balance:
            return "insufficient balance"

        else: 
            self.balance==totalwithdraw
            return "Hello {self.name},you have successfull transuctions and your balance is {self.balance}."

    def borrow(self,amount_loan):
        total=self.interest*amount_loan
        amount_loan=amount_loan+total
        if amount_loan>self.loan_bound:
            return f"Hello you have borrowed {self.loan} and your balance is {amount_loan-self.loan}."
        elif amount_loan<self.loon_bound:
            return "your loan amount is too much"
        elif amount_loan>0:
            return "you cannot borrow"
        else:
            now=datetime.now()
            transuction={
            "amount":amount_loan,
            "balance":self.balance,
            "naration":"You deposited",
            "time":now
             }
            self.loan_bound=total
            self.balance+= amount_loan
        return (f"Hello you have repayed {self.loan} and your balance is {amount_loan+self.loan}.")

# def get_statement(self):
#     for transuction in self.transuction:
#         amount=transuction["amount"]
#         narration=transuction["narration"]
#         balance=transuction["balance"]
#         time=transuction["time"]
#         date=transuction["date"]
#     print (f"{amount}....{date}.... {narration}.... {amount}....balance {balance}.")
 
def repay(self,amount_loan):
        if amount_loan <0:
            return f"Enter a valid amount"
        elif amount_loan<=self.loan:
            self.loan_bound-=amount_loan
        else:
            differ=amount_loan-self.loan_bound
            self.loan_bound=0
            return f"you have repaid  your loan and your balance is UGsh{self.loan_bound}"
        
            