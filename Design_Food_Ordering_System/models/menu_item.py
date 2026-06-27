from threading import Lock


class MenuItem:
    def __init__(self, id: str, name: str, description: str, price: float, category: str, restaurant_id: str):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.restaurant_id = restaurant_id
        self.is_available = True
        self.lock = Lock()

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_category(self):
        return self.category

    def get_restaurant_id(self):
        return self.restaurant_id

    def is_item_available(self):
        return self.is_available

    def set_availability(self, is_available: bool):
        with self.lock:
            self.is_available = is_available