class Order:
    customers_info: dict = {}
    meat_preference: dict = {}
    veg_preference: dict = {}
    total_recipe: int
    total_customer: int

    def __init__(self, customers_info: dict, meat_preference: dict, veg_preference: dict, total_recipe, total_customer):
        self.customers_info = customers_info
        self.meat_preference = meat_preference
        self.veg_preference = veg_preference
        self.total_recipe = total_recipe
        self.total_customer = total_customer


