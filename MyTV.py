class TV:
    def __init__(self, state, channel, volume): 
        self.state = state
        self.channel = channel
        self.volume = volume
                
    def switch_on_off(self):
        if self.state == 1:
            self.state = 0
            print("TV Switching Off...")
        else:
            self.state = 1
            print("TV Switching On...")
    def decrease_volume(self):
        self.volume = self.volume - 1
        print("TV volume decresed by 1, present volume [", self.volume, "]")
        
    def increase_volume(self):
        self.volume = self.volume + 1
        print("TV volume increased by 1, present volume [", self.volume, "]")
        
    def decrease_channel(self):
        self.channel = self.channel - 1
        print("TV channel decresed by 1, present channel [", self.channel, "]")
        
    def increase_channel(self):
        self.channel = self.channel + 1
        print("TV channel incresed by 1, present channel [", self.channel, "]")

    def goto_channel(self,newchannel):
        self.channel = newchannel
        print("TV channel changed, present channel [", self.channel, "]")


MyTV = TV(0, 100, 10)
MyTV.switch_on_off()
MyTV.increase_volume()
MyTV.decrease_volume()
MyTV.increase_channel()
MyTV.decrease_channel()
MyTV.goto_channel(200)
MyTV.switch_on_off()
del MyTV  


''' Assignemt 2 '''

class Account:
    def __init__(self, accno, accname, balance): 
        self.accno = accno
        self.accname = accname
        self.balance = balance
                
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit Failed, Amount [", amount, "] is not > 0!!!")
        else:
            self.balance = self.balance + amount
            print("Deposit successful for: ", amount)
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds!!!")
        else:
            self.balance = self.balance - amount
            print("Withdraw successful for: ", amount)


MyAccount = Account(12345, "Navya", 10)
MyAccount.withdraw(50)
MyAccount.deposit(15)
MyAccount.deposit(-100)
MyAccount.deposit(0)
MyAccount.withdraw(20)
del MyAccount  
