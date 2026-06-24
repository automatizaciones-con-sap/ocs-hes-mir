class Transaction:
    def __init__(self, code: str):
        self.code = code # ME21N

    def get_code(self):
        return self.code
    
    def get_info(self):
        return f"Transaction Code: {self.code}"