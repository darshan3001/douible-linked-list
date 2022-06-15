class Person:
    def __init__(self,name,number,college,dob):
        self.name = name
        self.number = number
        self.college = college
        self.dob = dob
    def details(self):
        print('\n Name : ',self.name,'\n', 'Phone Number : ',self.number,'\n', 'Name of college: ',self.college,'\n','Date of birth: ',self.dob,'\n')

d1 = Person('Darshan',8501088889,"GITAM",'06-08-2022')
d2 = Person('Srinivasu',9010858506,"Cocacola",'12-08-22')
d3 = Person('Sai Lakshmi',8501088888,'HouseWife','02-01-2022')
d1.details()
d2.details()
d3.details()