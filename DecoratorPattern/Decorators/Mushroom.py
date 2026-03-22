from Decorators.Toppings import Toppings

# Concrete implementation of Mushroom class
class Mushroom(Toppings):

    def get_cost(self):
        return self.base_pizza.get_cost() + 15