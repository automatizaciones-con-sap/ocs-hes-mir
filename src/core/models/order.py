from src.core.models.customer import Customer
from src.core.models.organization import Organization
from src.core.models.provider import Provider
from src.core.models.service import Service
from src.core.models.transaction import Transaction


class Order:
    def __init__(
            self, 
            type: str, # Low value
            number: str, # Is the ouput of the oc generation.
            date: str, # Optional to map the date of the order, for example: 2024-01-01
            state: str, # Is the state of the order, for example: 'PENDIENTE', 'PROCESADO', etc.
            customer: Customer,
            organization: Organization,
            provider: Provider,
            service: Service,
            transaction: Transaction
        ):
        self.type = type
        self.number = number
        self.date = date
        self.state = state
        self.customer = customer
        self.organization = organization
        self.provider = provider
        self.service = service
        self.transaction = transaction

    def get_info(self):
        return f"Order(type={self.type}, number={self.number}, date={self.date}, state={self.state},\ncustomer={self.customer.get_info()},\norganization={self.organization.get_info()},\nprovider={self.provider.get_info()},\nservice={self.service.get_info()},\ntransaction={self.transaction.get_info()})\n"

    def get_type(self):
        return self.type

    def get_number(self):
        return self.number
    
    def get_order_date(self):
        return self.date
        
    def get_state(self):
        return self.state
    
    def get_customer(self):
        return self.customer
    
    def get_organization(self):
        return self.organization
    
    def get_provider(self):
        return self.provider
    
    def get_service(self):
        return self.service
    
    def get_transaction(self): 
        return self.transaction.get_info()