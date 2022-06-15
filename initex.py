class system:
    def __init__(self,ram,cpu):
        self.ram = ram
        self.cpu = cpu
    def configuration(self):
        print('Configuration of the laptop is: ',self.ram,'and', self.cpu)

com1 = system(12,'i5')
com2 = system(4,'i5')
com1.configuration()
        