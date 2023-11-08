from abc import ABC, abstractclassmethod

class Beverage(ABC):
    """
    Component interface which defines methods for both components and
    decorators
    """
    @abstractclassmethod
    def describe(self):
        """
        Provides description of drink
        """
        pass

    @abstractclassmethod
    def calculate_cost(self):
        """
        returns cost of beverage
        """
        pass


class Coffee(Beverage):
    """
    Concrete component which implements the beverage class.
    """
    def __init__(self):
        self.cost = 1.00

    def describe(self):
        print(f"Coffee: {self.cost}")

    def calculate_cost(self):
        return self.cost
        

class Tea(Beverage):
    """
    Concrete component which implements the beverage class.
    """
    def __init__(self):
        self.cost = 0.90

    def describe(self):
        print(f"Tea: {self.cost}")

    def calculate_cost(self):
        return self.cost

class Condiment(Beverage):
    """
    Base decorator for
    """
    def __init__(self, beverage:Beverage):
        self.beverage = beverage

    def describe(self):
        self.beverage.describe()

    def calculate_cost(self):
        return self.beverage.calculate_cost()


class Sugar(Condiment):

    def __init__(self, beverage:Beverage):
        self.beverage = beverage
        self.cost = .25

    def describe(self):
        super().describe()
        print(f"Sugar: {self.cost}")

    def calculate_cost(self):
        return self.cost + super().calculate_cost()
    
class Milk(Condiment):
    def __init__(self, beverage:Beverage):
        self.beverage = beverage
        self.cost = .50

    def describe(self):
        super().describe()

        print(f"Milk: {self.cost}")

    def calculate_cost(self):
        return self.cost + super().calculate_cost()


    

if __name__ == "__main__":
    coffee = Coffee()
    coffee.describe()
    print(f"Total Cost: {coffee.calculate_cost()}")

    print("*****")

    coffee_with_milk = Milk(coffee)
    coffee_with_milk.describe()
    print(f"Total Cost: {coffee_with_milk.calculate_cost()}")

    print("*****")

    coffee_with_milk_and_sugar = Sugar(coffee_with_milk)
    coffee_with_milk_and_sugar.describe()
    print(f"Total Cost: {coffee_with_milk_and_sugar.calculate_cost()}")
