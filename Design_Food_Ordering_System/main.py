from models.customer import Customer
from models.delivery_agent import DeliveryAgent
from models.enums import OrderStatus, PaymentMethod, PromotionType
from models.location import Location
from models.menu_item import MenuItem
from models.order_item import OrderItem
from models.promotion import Promotion
from models.restaurant import Restaurant
from observers.notification_service import NotificationService
from services.order_service import OrderService
from services.rating_service import RatingService


if __name__ == "__main__":

    order_service = OrderService()
    rating_service = RatingService()
    notification_service = NotificationService()

    tandoorsLocation = Location(10.0, 20.0, "123 Oak St, Anytown, USA")
    leeLocation = Location(50.0, 10.0, "456 Main St, Anytown, USA")
    harryAgentLocation = Location(21.0, 10.0, "765 Pine St, Anytown, USA")

    tandoors = Restaurant("1", "Tandoors", "Indian", tandoorsLocation)

    tandoori = MenuItem("1", "Tandoori Chicken", "A crispy chicken dish", 10.0, "Main Course", "1")
    naan = MenuItem("2", "Naan", "A crispy bread dish", 5.0, "Side", "1")
    boti = MenuItem("3", "Boti", "A crispy chicken dish", 15.0, "Main Course", "1")

    tandoors.add_menu_item(tandoori)
    tandoors.add_menu_item(naan)
    tandoors.add_menu_item(boti)

    lee = Customer("2", "Lee", "lee@example.com", "1234567890", leeLocation)
    harry = DeliveryAgent("3", "Harry", "1234567890", harryAgentLocation)

    order_items = [
        OrderItem("1", tandoori, 2),
        OrderItem("2", naan, 3),
    ]

    order = order_service.create_order(lee, tandoors, order_items, leeLocation)
    order.add_observer(notification_service)

    print(f"Order created: {order.get_id()}. Subtotal: {order.calculate_subtotal()}, Total: {order.calculate_total()}. Status: {order.get_status().value}")

    promotion = Promotion("1", "SAVE10", PromotionType.PERCENTAGE_DISCOUNT, 10.0)
    order_service.apply_promotion(order, promotion)

    print(f"Promotion applied: {order.get_promotion().get_id()}. Discount: {order.calculate_discount()}")

    payment_details = {
        "card_number": "1234567890",
        "cvv": "123",
        "expiry_date": "2026-01-01",
    }

    payment = order_service.process_payment(order, PaymentMethod.CREDIT_CARD, payment_details)
    print(f"Payment processed: {payment.get_id()}. Status: {payment.get_status().value}")
    print(f"Order status: {order.get_status().value}")

    order_service.update_order_status(order, OrderStatus.CONFIRMED)
    print(f"Order status: {order.get_status().value}")

    order_service.assign_delivery_agent(order, [harry])
    print(f"Delivery agent assigned: {order.get_delivery_agent().get_name()}")
 
    order_service.update_order_status(order, OrderStatus.PREPARING)
    print(f"Order status: {order.get_status().value}")

    order_service.update_order_status(order, OrderStatus.OUT_FOR_DELIVERY)
    print(f"Order status: {order.get_status().value}")

    order_service.update_order_status(order, OrderStatus.DELIVERED)
    print(f"Order status: {order.get_status().value}")

    rating_service.rate_restaurant(lee, tandoors, 5, "Great food and service")
    rating_service.rate_delivery_agent(lee, harry, 5, "Great delivery service")

    print(f"Restaurant rating: {tandoors.get_average_rating()}")
    print(f"Delivery agent rating: {harry.get_average_rating()}")
    

