class bike:
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