import dataclasses

from app.car import Car


@dataclasses.dataclass
class Customer:
    name: str
    product_card: dict
    location: list[int]
    money: float | int
    car: Car

    @staticmethod
    def get_customer_list(config: dict) -> list:
        customer_list = config.get("customers")
        result = []

        for customer in customer_list:
            result.append(
                Customer(
                    customer["name"],
                    customer["product_cart"],
                    customer["location"],
                    customer["money"],
                    Car(
                        customer["car"]["brand"],
                        customer["car"]["fuel_consumption"]
                    )
                )
            )

        return result
