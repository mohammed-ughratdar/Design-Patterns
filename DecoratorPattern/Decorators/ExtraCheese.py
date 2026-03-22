from Decorators.Toppings import Toppings

# Concrete implementation of ExtraCheese class
class ExtraCheese(Toppings):

    def get_cost(self):
        return self.base_pizza.get_cost() + 10