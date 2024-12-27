class car:
    def __init__(self,name): ##Self is necessary
        self.name=name
    def display(self): 
        print("My favourite Car is",self.name)
car1=car("BMW 325i")
car1.display()
car2=car("Mercedes Benz")
car2.display()