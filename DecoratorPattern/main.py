from Margharita import Margharita
from BombaySupreme import BombaySupreme
from MexicanBomb import MexicanBomb
from Decorators.ExtraCheese import ExtraCheese
from Decorators.Mushroom import Mushroom
from Decorators.FriedOnions import FriedOnions
from Decorators.GarlicOil import GarlicOil

def main():
    margharita = Margharita()
    print(f"Margharita cost: {margharita.get_cost()}")
    extra_cheese = ExtraCheese(margharita)
    print(f"Margharita with Extra Cheese cost: {extra_cheese.get_cost()}")
    mushroom = Mushroom(extra_cheese)
    print(f"Margharita with Extra Cheese and Mushroom cost: {mushroom.get_cost()}")
    fried_onions = FriedOnions(mushroom)
    print(f"Margharita with Extra Cheese and Mushroom and Fried Onions cost: {fried_onions.get_cost()}")
    garlic_oil = GarlicOil(fried_onions)
    print(f"Margharita with Extra Cheese and Mushroom and Fried Onions and Garlic Oil cost: {garlic_oil.get_cost()}")
    
    print(f"Total cost: {garlic_oil.get_cost()}")
if __name__ == "__main__":
    main()