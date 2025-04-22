class Cyclist:
    def __init__(self):
        self.name = "Jake Rohan"
        self.age = 35
        self.weight = 105
        self.proficiency = "Mountain"
        self.protective_gear = False

    def accelerate(self):
        print("Got to go fast.")

    def apply_brakes(self):
        print("Stopping!")

    def turn(self, direction):
        print(f"Turning {direction}")

    def wear_protective_gear(self):
        self.protective_gear = True
        print("Protective gear is now on.")