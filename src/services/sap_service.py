import os
import time
import subprocess
import win32com.client
from dotenv import load_dotenv

class SapService:
    # Constructor
    def __init__(self):
        load_dotenv() # Load environment variables from .env file
        self.user = os.getenv("USER_SAP") # Get the SAP user from environment variables
        self.password = os.getenv("PASSWORD_SAP") # Get the SAP password from environment variables
        self.server = os.getenv("SERVER_SAP") # Get the SAP server from environment variables
        self.client = os.getenv("CLIENT_SAP") # Get the SAP client from environment variables
        self.path = os.getenv("PATH_SAP") # Path to SAP Logon executable
        self.session = None    # Close other SAP session
    
    # Method to connect to SAP session
    def connect_sap(self):
        try: 
            # Execute saplogon.exe
            sap_path = self.path
            subprocess.Popen(sap_path) # Open SAP Logon
            time.sleep(5) # Wait for SAP Logon to open

            # Connect to scripting engine
            sap_gui_auto = win32com.client.GetObject("SAPGUI") # Open SAP GUI
            application = sap_gui_auto.GetScriptingEngine # Get the scripting engine

            # 3. Connect to the first connection and session
            connection = application.OpenConnection(self.server, True) # Open the specified connection
            self.session = connection.Children(0) # Get the first session

            # 4. Log in to SAP session
            self.session.findById("wnd[0]/usr/txtRSYST-BNAME").text = self.user
            self.session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = self.password
            self.session.findById("wnd[0]/usr/txtRSYST-MANDT").text = self.client
            self.session.findById("wnd[0]").sendVKey(0)
            print("Connected to SAP session successfully.")
            return True
        except Exception as e:
            print(f"Error connecting to SAP session: {e}")
            return False
        
    # Method to enter to a transaction code
    def enter_to_transaction(self, transaction_code):
        """Enter to the transaction code in the SAP session"""
        if self.session: # Check if the session is connected
            self.session.findById("wnd[0]/tbar[0]/okcd").text = transaction_code # Enter the transaction code
            self.session.findById("wnd[0]").sendVKey(0) # Press Enter
            print(f"Entered transaction code: {transaction_code}")
        else:
            print("No SAP session connected. Please connect to a session first.")

    def get_session(self):
        return self.session