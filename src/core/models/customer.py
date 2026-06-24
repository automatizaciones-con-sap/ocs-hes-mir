# Markets or stations
class Customer:
    def __init__(self, sap_code: str, name: str, applicant_code: str):
        self.sap_code = sap_code # P111
        self.name = name
        self.applicant_code = applicant_code

    def get_info(self):
        return f"Customer(sap_code={self.sap_code}, name={self.name}, applicant_code={self.applicant_code})"
    
    def get_sap_code(self):
        return self.sap_code

    def get_name(self):
        return self.name
    
    def get_applicant_code(self):
        return self.applicant_code
