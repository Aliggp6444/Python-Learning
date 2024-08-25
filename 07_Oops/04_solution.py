class Car:
      def __init__(self, userbrand, usermodel):
            self.__brand = userbrand
            self.model = usermodel
      def get_brand(self):
            return self.__brand + " !"
            
      def full_name(self):
            return f"{self.__brand} -- {self.model}"
      
my_car = Car("Toyota","Corolla")

class ElectricCar(Car):
      def __init__(self, userbrand, usermodel, battery_size):
            super().__init__(userbrand, usermodel)
            
            self.battery_size = battery_size
            
my_batter_car = ElectricCar("Tesla", "Model S", "85kwh")

# print(my_batter_car.__brand)  # Not accessible as it's a private 
print(my_batter_car.get_brand())  