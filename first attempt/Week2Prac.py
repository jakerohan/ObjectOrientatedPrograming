class Bike:
    def __init__(self):
        self.type = "Mountain Bike"
        self.max_gears = 6
        self.gear = 1

    def change_gear(self, increase_gear):
        if increase_gear:
            if self.gear < self.max_gears:
                self.gear += 1
                print(f"Gear increased to: {self.gear}")
            else:
                print("Gear could not be changed.")
        else:
            if self.gear > 1:
                self.gear -= 1
                print(f"Gear decreased to: {self.gear}")
            else:
                print("Gear could not be changed.")

class Cyclist:
    def __init__(self):
        self.name = "Jake Rohan"
        self.age = 35
        self.weight = 105
        self.proficiency = "Mountain"
        self.protective_gear = False

    def accelerate(self):
        print("Got to go fast.")

    def brake(self):
        print("Stopping!")

    def turn(self, direction):
        print(f"Turning {direction}")

    def wear_protective_gear(self):
        self.protective_gear = True
        print("Protective gear is now on.")