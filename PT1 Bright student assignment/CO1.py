class Employee:
    def __init__(self, level, empno, basicpay):
        self.level = level
        self.empno = empno
        self.basicpay = basicpay
    
    def calcperks(self):
        perks = {
            1: 1500,
            2: 950,
            3: 600,
            4: 250
        }
        self.perks = perks.get(self.level)

    def calchouserenet(self):
        self.houserent = 0.25 * self.basicpay

    def calcgross(self): #Gross salary = basic pay + house rent allowance + perks
        self.gross = self.basicpay + self.houserent + self.perks

    def incometax(self): 
        income_tax_dict  = {
        range(0, 2001) : 0,
        range(2001, 4001) : 0.3,
        range(4001, 5001) : 0.5,
        range(5001, 99999): 0.8
        }
        for income_range in income_tax_dict.keys():
            if self.gross in income_range:
                self.incometax = income_tax_dict[income_range] * self.basicpay
    
    def calcnet(self):
        self.net = self.gross - self.incometax
    def getdata(self):
        print("---------------------------------\n"
              f"Executive Job Number: {self.empno}\n"
              f"Level = {self.level}\n"
              f"Gross Salary = {self.gross}\n"
              f"Net Salary = {self.net}\n")
emp1 = Employee(1, 59, 5000)
emp1.calcperks()
emp1.calchouserenet()
emp1.calcgross()
emp1.incometax()
emp1.calcnet()
emp1.getdata()
emp_num = int(input("Enter number of employees: "))
for i in range(emp_num):
    level1 = int(input("Enter Level: "))
    empno1 = input("Enter Empno: ")
    basicpay1 = int(input("Enter Basic pay: "))
    i = Employee(level1, empno1, basicpay1)
    i.calcperks()
    i.calchouserenet()
    i.calcgross()
    i.incometax()
    i.calcnet()
    i.getdata()