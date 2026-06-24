class Service:
    def __init__(
            self, 
            i: str, 
            p: str, 
            name: str, 
            article_group: str,
            num_service: str,
            quantity: int,
            # Price without igv
            gross_price: float,
        ):
        self.i = i
        self.p = p
        self.name = name
        self.article_group = article_group
        self.num_service = num_service
        self.quantity = quantity
        self.gross_price = gross_price

    def get_info(self):
        return f"Product(i={self.i}, p={self.p}, name={self.name}, article_group={self.article_group})"
    
    def get_i(self):
        return self.i
    
    def get_p(self):
        return self.p
    
    def get_name(self):
        return self.name
    
    def get_article_group(self):
        return self.article_group
        
    def get_num_service(self):
        return self.num_service
    
    def get_quantity(self):
        return self.quantity
    
    def get_gross_price(self):
        return self.gross_price