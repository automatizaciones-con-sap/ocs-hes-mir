import pandas as pd
import os
from dotenv import load_dotenv

class SharePointService:
    def __init__(self):
        load_dotenv()
        self.excel_sp_path = os.getenv("PATH_EXCEL_SP")
    
    def get_data_from_excel(self):
        try:
            if not os.path.exists(self.excel_sp_path):
                raise FileNotFoundError(f"Excel file not found at path: {self.excel_sp_path}")
            df = pd.read_excel(self.excel_sp_path, sheet_name='INPUT')
            return df
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None