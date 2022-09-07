import json
from datetime import date
from random import randint
from app.models.Customer import Customer
from app.models.Notification import Notification

class Account( Customer ) :
    
    # Constructor
    def __init__( self, first_name: str, last_name: str, date_of_birth: date, phone_number: str, email_address: str, residential_address: str, middle_name = "", postal_address = "" ) :

        # Validate the data from the user (Pending)

        # Calling the constructor (__init__()) method from the parent class
        super().__init__( first_name, last_name, date_of_birth, phone_number, email_address, residential_address, middle_name, postal_address )

    def create_account( self ) :

        # Call the (create_customer) from the super class
        customer = super().create_customer()

        # Check if the (create_customer) has been created successfully
        if customer != False :
            account = { "id": randint(100, 999), "customer_id": customer["id"], "account_number": randint(1000000000, 9999999999), "account_type": "", "account_currency": "", "current_balance": 0.00, "available_balance": 0.00, "status": "Active" }
            self.write_to_accounts_file( account )

            # Send email to customer 
            Notification.send_email( customer["name"], customer["email"], "Create Account" )

        # Cannot create the customer. Return fales
        else :
            return False

    def credit_account( self ) :
        pass

    def debit_account( self ) :
        pass

    def check_balance( self ) :
        pass

    def delete_account( self ) :
        pass

    @staticmethod
    def write_to_accounts_file( account_data ) :

        # Open the JSON file
        with open( "storage/accounts.json", "r+" ) as json_file :

            # Load the JSON file into Python Dict
            file_data = json.load( json_file )

            # Add the account_data into the file_data(JSON converted to dict)
            file_data["accounts"].append( account_data )

            # Sets file's current position at offset
            json_file.seek(0)

            # convert back to json
            json.dump( file_data, json_file, indent = 4 )

            return True

