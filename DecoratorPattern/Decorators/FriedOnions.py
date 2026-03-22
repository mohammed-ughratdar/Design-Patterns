from Decorators.Toppings import Toppings

# Concrete implementation of FriedOnions class
class FriedOnions(Toppings):
    def get_cost(self):
        return self.base_pizza.get_cost() + 20