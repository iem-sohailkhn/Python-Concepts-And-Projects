class Programmers:
    company = "Microsoft"
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
    
    def getinfo(self):
      print("------------------------------------------------------------------------------")
      print(f"The Name Of Programmer {self.name}\nThe Company Name Is {self.company}\nThe Salary Of {self.name} is {self.salary}\nThe LAnguage is {self.language}")

p = Programmers("Sohail",12000,"Python")
p.getinfo()
# print(p.company,p.name,p.salary,p.language)
s= Programmers("Jibran",15000,"Js")
s.getinfo()
# print(s.company,s.name,s.salary,s.language)


    