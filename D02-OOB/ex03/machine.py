#!/usr/bin/python3

from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random

class CoffeeMachine:
    def __init__(self):
        self.served = 0
        self.max_served = 10

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__(price=0.90, name="empty cup")
        def description(self):
            return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.served = 0
        return "... coffee machine repaired!"

    def serve(self, beverage):
        if self.served >= self.max_served:
            raise self.BrokenMachineException()
        self.served += 1

        return random.choice([beverage(), self.EmptyCup()])

if __name__ == "__main__":
    def test_coffeemachine():
        machine = CoffeeMachine()
        beverages = [Coffee, Tea, Chocolate, Cappuccino]
        try:
            for _ in range(12):
                drink = machine.serve(random.choice(beverages))
                print(drink)
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            print(machine.repair())

    test_coffeemachine()
