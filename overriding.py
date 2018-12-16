class Employee:
    def noOfwrk_hrs(self):
        self.wrk_hrs = 40

    def showwrk_hrs(self):
        print(self.wrk_hrs)

class Trainee(Employee):
    def noOfwrk_hrs(self):
        self.wrk_hrs = 45

    def resetnormalhrs(self):
         super().noOfwrk_hrs()

Tom = Employee()
Tom.noOfwrk_hrs()
print("Employee normal working hours:", end='')
Tom.showwrk_hrs()

Pradeep = Trainee()
Pradeep.noOfwrk_hrs()
print("Trainee working hours:" , end='')
Pradeep.showwrk_hrs()


Pradeep.resetnormalhrs()
print("Trainee work hours as normal employee:", end='')
Pradeep.showwrk_hrs()