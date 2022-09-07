from datetime import date
import json
from random import randint

class Customer() :
    
    # Constructor
    def __init__( self, first_name: str, last_name: str, date_of_birth: date, phone_number: str, email_address: str, residential_address: str, middle_name = "", postal_address = "" ) :

        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__phone_number = phone_number
        self.__email_address = email_address
        self.__residential_address = residential_address
        self.__postal_address = postal_address

    def create_customer( self ) :

        # Create a dictionary type data with the customer info and serilize the json data
        customer = { 
            "id": randint(100, 999), 
            "first_name": self.__first_name, 
            "middle_name": self.__middle_name, 
            "last_name": self.__last_name, 
            "date_of_birth": self.__date_of_birth, 
            "phone_number": self.__phone_number, 
            "email_address": self.__email_address, 
            "residential_address": self.__residential_address, 
            "postal_address": self.__postal_address, "status" : "Active" }

        # Return the customer_id if successful 
        return self.write_to_customers_file( customer )
        
    def get_customer( self ) :
        customer = { "name": self.__first_name + " " + self.__last_name, "email": self.__email_address, "date_of_birth": self.__date_of_birth, "phone_number": self.__phone_number, "postal_address": self.__postal_address, "residential_address": self.__residential_address }
        return customer

    def update_customer( self ) :
        pass

    def update_customer_status( self ) :
        pass

    def delete_customer( self ) :
        pass

    @staticmethod
    def write_to_customers_file( customer_data ) :

        # Open the JSON file
        with open( "storage/customers.json", "r+" ) as json_file :

            # Load the JSON file into Python Dict
            file_data = json.load( json_file )

            # Add the customer_data into the file_data(JSON converted to dict)
            file_data["customers"].append(customer_data)

            # Sets file's current position at offset
            json_file.seek(0)

            # convert back to json
            json.dump( file_data, json_file, indent = 4 )

            # Return the customer id
            return { "id": customer_data["id"], "name": customer_data["first_name"] + " " + customer_data["last_name"], "email": customer_data["email_address"] }

