from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train No {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"The Train is Running on time..")
    def getFare(self,fro,to):
        print(f"Ticket fare in train Number {self.trainNo} from {fro} to {to} is {randint(222,66666)}")

t = Train(1234)
t.book("Islamabad","Mansehra")
t.getstatus()
t.getFare("Islamabad","Mansehra")
        