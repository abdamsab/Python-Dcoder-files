#python 3.7.1

class Account():
  
  def __init__ (self, owner, balance):
    self.owner = owner
    self.balance = balance
    
  def deposit(self, amount):
    if amount <= 0:
      print('Invalid amount')
    else:
      self.balance = self.balance + amount
      print('Deposit accepted. New balance: {}'.format(self.balance))
      
  def withdraw(self, amount):
    if self.balance - amount < 0:
      print('Insufficient balance')
    else:
      self.balance = self.balance - amount
      print('Withdraw accepted. New balance: {}'.format(self.balance))
   
  def __str__(self):
     return ('Account owner: ' + self.owner + '\n' +
            'Account balance: ' + str(self.balance))
            
            
acct1 = Account('Damisa', 200)

print(acct1)
acct1.owner
acct1.balance

acct1.deposit(130)
acct1.withdraw(150)

acct1.withdraw(800)
     