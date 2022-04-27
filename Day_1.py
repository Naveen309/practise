                          # ------------------------------CAR INFO--------------------------



class car:
    def __init__(self,manufacturer_name,price,type_of_fuel,model,releasing_year):
        self.manufacturer_name=manufacturer_name
        self.price=price
        self.type_of_fuel=type_of_fuel
        self.model=model
        self.releasing_year=releasing_year
class car1(car):
    def car_info1(self):
        pass
class car2(car1):
    def car_info2(self):
        print(f"The manufacturer name is:{self.manufacturer_name}\nThe price of the car is:{self.price}\nThe type of fuel is:{self.type_of_fuel}\nThe model is:{self.model}\nThe res=leasing year is:{self.releasing_year}")

print("****************Tesla car specifications***************")
carinf1=car2("Tesla","$100000","Battery","T4","2022")
carinf1.car_info2()
print("****************Hyundai car specifications***************")
carinf2=car2("Hyundai","$58456","Diesel","i20","2020")
carinf2.car_info2()
print("****************Maruthi car specifications***************")
carinf3=car2("Maruthi","$28456","Petrol","shift","2017")
carinf3.car_info2()



             # -----------------------------------GENERATE RANDOM PROFILE------------------------------------

import random

first_name = ["Naveen","Nageshwarao","Lakshmi","Nalini","Nagalatha","Manoj"]
last_name = ["chilaka","kedhari","gopisetty"]
street_names = ["sri nagar colony","avilala","m.r.palli","vikunrapuram"]
cities = ["tirupathi","bangalore","nellore","Hyderabad"]
states = ["AP","KS","TS"]
class Name:
    def __init__(self, num=1):
        self.num = num

    def first_name(self):
            first = random.choice(first_name)
            pass

    def last_name(self):
            last = random.choice(last_name)
            pass

    def full_name(self):
            first = random.choice(first_name)
            last = random.choice(last_name)
            full_name=first+last
            pass

    def full_profile(self):
            first = random.choice(first_name)
            last = random.choice(last_name)
            street = random.choice(street_names)
            city = random.choice(cities)
            state = random.choice(states)
            print(f"First Name:{first}\nLast Name:{last}\nStreet:{street}\nCity:{city}\nState:{state}")

a=Name()
a.full_profile()
a.first_name()
a.last_name()
a.full_name()


                # '''------------------------------------------Atm senario----------------------------------'''

# class Atm:
#     bank_name="State Bank Of India"
#     print(f"WELCOME TO {bank_name}")
#
#     def __init__(self,balance):
#         self.balance=balance
#
#     def pin_number(self,pinNumber):
#         PinNumber=int(input("Enter your pin Number:"))
#         if PinNumber==1111:
#             return True
#         else:
#             print(f"Your Entered Wrong Pin")
#             return False
#
#     def deposit(self,depositamount=int(input("enter deposit amount:"))):
#         # self.depositamount=depositamount
#         # total= self.Minbalance + self.depositamount
#         # return True
#           self.balance+=depositamount
#
#     def withdrawl(self,withdraw=int(input("enter withdraw amount:"))):
#        if  self.balance>=withdraw:
#            self.balance-=withdraw
#        else:
#            print("insufficient funds")
#
#     # def currentbalance(self,availablebalance):
#     #     availablebalance=Minbalance-withdrawamount
#     #     print(f"{availablebalance}")
# a=Atm()
# # a.currentbalance()
# a.withdrawl()
# a.deposit()
# a.min_balance(500)
# a.pin_number(1111)

