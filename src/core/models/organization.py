class Organization:
    def __init__(
            self, 
            purchase_organization_code: str, #PE20
            purchase_organization: str, #U03
            society_code: str#PE02
        ):
        self.purchase_organization_code = purchase_organization_code
        self.purchase_organization = purchase_organization
        self.society_code = society_code
    
    def get_info(self):
        return f"Organization(purchase_organization_code={self.purchase_organization_code}, purchase_organization={self.purchase_organization}, society_code={self.society_code})"
    
    def get_purchase_organization_code(self):
        return self.purchase_organization_code
    
    def get_purchase_organization(self):
        return self.purchase_organization
    
    def get_society_code(self):
        return self.society_code