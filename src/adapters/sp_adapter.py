import pandas as pd
import os
from dotenv import load_dotenv

class SharePointAdapter:
    def __init__(self):
        load_dotenv()
        self.path = os.getenv("PATH_EXCEL_SP")


    def read_excel_file_from_sharepoint(self):
        try:
            if not os.path.exists(self.path):
                print(f"File not found at path: {self.path}")
                return None
            return pd.read_excel(self.path, sheet_name="INPUT")
        except Exception as e:
            print(f"Error reading Excel file from SharePoint: {e}")
            return None