from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Dave.deposit(500)

Dave.withdraw(10)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.getBalance()

Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(100, Sara)
Blaze.transfer(10000, Sara)
