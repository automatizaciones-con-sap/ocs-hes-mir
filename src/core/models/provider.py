class Provider:
    def __init__(self, name: str, identifier: str, cost_center: str):
        self.name = name
        self.identifier = identifier
        self.cost_center = cost_center # Depends of the society code, for example: PE02

    def get_info(self):
        return f"Provider(name={self.name}, identifier={self.identifier}, cost_center={self.cost_center})"

    def get_name(self):
        return self.name

    def get_identifier(self):
        return self.identifier
    
    def get_cost_center(self):
        return self.cost_center