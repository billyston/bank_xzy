from app.models.Account import Account


# Create the account object and call the create_account method
customer1 = Account( "Michael", "Katey", "1982-07-02", "0244637602", "billyston@gmail.com", "140, Lakeside, Adenta - Accra" )
# customer1.create_account()

# Get customer
print(customer1.get_customer())

# Credit account