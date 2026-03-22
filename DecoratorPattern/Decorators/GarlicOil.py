from Decorators.Toppings import Toppings

# Concrete implementation of GarlicOil class
class GarlicOil(Toppings):
    def get_cost(self):
        return self.base_pizza.get_cost() + 2