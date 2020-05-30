class FoodOrder:
    Name = 'No name Provided'
    Order_Number = 0
    Item_Ordered = ''
    Customer_Coupon = ''
    Price = ''

class EmployeeFreeOrder(FoodOrder):
    EmployeeName = 'No name Provided'
    OnDutyDiscount = '100%'
    ManagerID = '666'

class EmployeeDiscountOrder(FoodOrder):
    EmployeeName = 'No name Provided'
    EmployeeID = '1234'
    Item_Ordered = ''
    OffDutyDiscount = '50%'
    
    
    
    
