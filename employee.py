"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from abc import ABC, abstractmethod

class Commission(ABC):
    @abstractmethod
    def calculate_pay(self):
        return 0
    
    @abstractmethod
    def __str__(self):
        return ""

class NoCommission(Commission):
    def calculate_pay(self):
        return super().calculate_pay()
    
    def __str__(self):
        return super().__str__()

class FixedCommission(Commission):
    def __init__(self, rate):
        self.rate = rate
    
    def calculate_pay(self):
        return self.rate
    
    def __str__(self):
        return f" and receives a bonus commission of {self.rate}"

class VariableCommission(Commission):
    def __init__(self, rate, contracts):
        self.rate = rate
        self.num_of_contracts = contracts

    def calculate_pay(self):
        return self.rate*self.num_of_contracts

    def __str__(self):
        return f" and receives a commission for {self.num_of_contracts} contract(s) at {self.rate}/contract"
    
class Contract(ABC):
    @abstractmethod
    def calculate_pay(self):
        return 0
    
    @abstractmethod
    def __str__(self):
        return ""
    
class HourlyContract(Contract):
    def __init__(self, rate, hours_worked=0):
        self.rate = rate
        self.hours_worked = hours_worked
    
    def calculate_pay(self):
        return self.rate*self.hours_worked
    
    def __str__(self):
        return f"contract of {self.hours_worked} hours at {self.rate}/hour"

class MonthlyContract(Contract):
    def __init__(self, rate):
        self.rate = rate

    def calculate_pay(self):
        return self.rate
    
    def __str__(self):
        return f"monthly salary of {self.rate}"
    
    
class Employee:
    def __init__(self, name, contract, comission):
        self.name = name
        self.contract: Contract = contract
        self.commision: Commission = comission
        self.pay = self.contract.calculate_pay() + self.commision.calculate_pay()

    # Potential extension needed(in a real app)
    def update_pay(self):
        pass
    
    def get_pay(self):
        return self.pay

    def __str__(self):
        _string = f"{self.name} works on a {self.get_var_string()}. Their total pay is {self.pay}."
        return _string
    
    def get_var_string(self):
        return f"{self.contract}{self.commision}"


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', contract=MonthlyContract(4000), comission=NoCommission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(rate=25, hours_worked=100), NoCommission())


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyContract(3000), VariableCommission(rate=200, contracts=4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), VariableCommission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyContract(2000), FixedCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), FixedCommission(600))


print(str(billie))
print(charlie)
print(renee)
print(jan)
print(robbie)
print(ariel)