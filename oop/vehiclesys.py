class Vehicle:
    total =0
    isrented=False
    @classmethod
    def tot(cls):
        cls.total+=1
    @classmethod
    def get_tot(cls):
        print(f"total vehicles are {cls.total}")
    def __init__(self,id,brand,model,rentalPricePerDay):
        self.id= id 
        self.brand=brand
        self.model=model
        self.rentalPricePerDay=rentalPricePerDay
        Vehicle.tot()
    def rent(self):
        self.isrented=True
        return self.isrented
    def returnV(self):
        self.isrented=False
        return self.isrented
    def calc_rent(self, day):
        return day*self.rentalPricePerDay
    def get_details(self):
        print(f"{self.id}, brand: {self.brand},model: {self.model},\n rent per day for {self.rentalPricePerDay},\n status:{self.isrented}")        
class car(Vehicle):
    def __init__(self,id,brand,model,rentalPricePerDay,numDoors):
        super().__init__(id,brand,model,rentalPricePerDay)
        self.numDoors=numDoors

class Motorcycle(Vehicle):
    def __init__(self,id,brand,model,rentalPricePerDay,engine):
        super().__init__(id,brand,model,rentalPricePerDay*7)
        self.engine=engine
class Truck(Vehicle):
    def __init__(self,id,brand,model,rentalPricePerDay, capacity):
        super().__init__(id,brand,model,rentalPricePerDay)
        self.capacity=capacity
carr = car("V001", "Toyota", "Camry", 50, 4)
motorcycle = Motorcycle("V002", "Harley", "Street 750", 40, 750)
truck = Truck("V003", "Ford", "F-150", 80, 2.5)
carr.get_details()
print(carr.returnV())
cost = carr.calc_rent(5)
print(f"Rental cost for 5 days: ${cost}")
carr.get_tot()