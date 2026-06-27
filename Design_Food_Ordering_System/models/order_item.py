from models.menu_item import MenuItem


class OrderItem:
    def __init__(self, id: str, menu_item: MenuItem, quantity: int):
        self.id = id
        self.menu_item = menu_item
        self.quantity = quantity

    def get_id(self):
        return self.id

    def get_menu_item(self):
        return self.menu_item
        
    def get_subtotal(self):
        return self.menu_item.get_price() * self.quantity
        