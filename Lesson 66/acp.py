class BMW:
    def fuel_type(self):
        print("BMW uses Petrol or Diesel.")

    def speed(self):
        print("BMW has high speed performance.")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Premium Petrol.")

    def speed(self):
        print("Ferrari is extremely fast.")

for car in (BMW(), Ferrari()):
    car.fuel_type()
    car.speed()
    print()