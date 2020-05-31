
# Parent Class
class Person:
    name = "Felts"
    email = "felts@gmail.com"
    password = "123456"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

# Child Class Customer
class Customer(Person):
    creditdebit = "4456 5454 3452"
    securecode = "123"
    expdate = "6/27"
    clubid = "1234"
    cardpin = "5941"

    def getLoginInfo(customer):
        entry_clubid = input("Enter your Club Id: ")
        entry_cardpin = input("Enter your accounts linked card pin: ")
        if (entry_clubid == customer.clubid and entry_cardpin == customer.cardpin):
            print("Welcome back, {}! Thank you for using express checkout!".format(entry_clubid))
        else:
            print("The club id or card pin is incorrect.")
            
# Child Class Employee
class Employee(Person):
    base_pay = 12.50
    department = "Deli"
    employeeid = "4444"
    timein = "12:00"

    
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_timein = input("Enter when you clocked in: ")
        entry_employeeid = input("Enter your Employee ID: ")
        if (entry_timein == self.timein and entry_employeeid == self.employeeid):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The employee id is incorrect or you missed your shift.")
    
Person = Person()
Person.getLoginInfo()
    
Customer = Customer()
Customer.getLoginInfo()

Employee = Employee()
Employee.getLoginInfo()
