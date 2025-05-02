class Calculator:
    def __init__(self,number):
        self.number=number

    def sq_of_no(self):
        print(f"The square of number is {self.number*self.number}")

    def cb_of_no(self):
        print(f"The Cube Of number is {self.number ** 3}")
    
    def cbr_of_no(self):
        print(f"The cube root of number is {self.number ** (1/3)}")

s = Calculator(4)
s.sq_of_no()
s.cb_of_no() 
s.cbr_of_no()