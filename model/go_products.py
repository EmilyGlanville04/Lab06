from dataclasses import dataclass

@dataclass
class Go_Products:
    product_number:int
    product_line:str
    product_type:str
    product:str
    product_brand:str
    product_color:str
    unit_cost: float
    unit_price:float

    def __eq__(self, other):
        return self.product_number == other.product_number

    def __hash__(self):
        return hash(self.product_number)

    def __str__(self):
        return f"{self.product_number} - {self.product} - {self.product_brand} "

