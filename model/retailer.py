from dataclasses import dataclass

@dataclass
class Retailer:
    retailer_code: int
    retailer_name: str
    type: str
    country: str

    def __hash__(self):
        return hash(self.retailer_code)

    def __str__(self):
        return f"{self.retailer_name}"