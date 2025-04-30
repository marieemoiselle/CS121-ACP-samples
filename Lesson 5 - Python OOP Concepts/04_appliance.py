from abc import ABC, abstractmethod
# Appliance class
class Appliance(ABC):
    #Constructor of Appliance
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power
        self.is_on = False
    
    # Method to turn the appliance ON
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"The appliance {self.brand} is now running.")
        else:
            print(f"The appliance {self.brand} is already on.")
    
    # Method to turn the appliance OFF
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"The appliance {self.brand} has been turned off.")
        else:
            print(f"The appliance {self.brand} is already off.")
    
    # Get the brand name of the appliance
    def get_brand(self):
        return self.brand
    
    # Get the power (wattage)
    def get_power(self):
        return self.power
    
    @abstractmethod
    def operate(self):
        pass

# Subclass of Appliance
class WashingMachine(Appliance):
    def __init__(self, brand, power, load_capacity):
        super().__init__(brand, power)
        self.load_capacity = load_capacity

    # Implementation of operate method from parent
    def operate(self):
        print(f"Operating the {self.brand} washing machine")

    # Specialized method for washing machine
    def start_wash_cycle(self):
        if self.is_on:
            print(f"{self.brand} is washing a {self.load_capacity}kg load.")
        else:
            print(f"Turn on the {self.brand} washing machine first.")

# Creation of Appliance Objects
# appliance1 = Appliance("LG", 1200)
# appliance1.turn_on()
# appliance1.turn_off()
# appliance1.turn_off()

washing_machine1 = WashingMachine("Whirlpool", 1800, 7)
washing_machine1.start_wash_cycle()
washing_machine1.turn_on()
washing_machine1.operate()
washing_machine1.start_wash_cycle()
washing_machine1.turn_off()