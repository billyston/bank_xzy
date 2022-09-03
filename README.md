# bank_xzy
This is to test my knowledge in Python OOBanking Application (Bank ZXY)

1. Modules and Attributes
1. Customer
	1. id_number
	2. first_name
	3. middle_name
	4. last  / surname
	5. date_of_birth
	6. phone_number
	7. postal_address
	8. residential_address
	9. status
	   
2. Account
	1. id
	2. customer_id
	3. account_number
	4. account_type
	5. account_currency
	6. current_balance
	7. available_balance
	8. status (active, suspended)
	   
3. Transactions
	1. id
	2. account_id
	3. transaction_type (debit, credit, transfer)
	4. transaction_amount
	5. charges
	6. total
	7. narration
	8. status (success, failed, canceled, pending)
	   
4. Notifications
	1. id
	2. send_email
	3. receiver_email
	4. message_body
	5. status (sent, failed)

2. Functions
1. Customer
	1. Create new customer
	2. Edit / Update customer
	3. Delete customer
	4. Change customer status
	   
2. Account
	1. Create new account 
	2. Credit account
	3. Debit account
	4. Check balance
	   
3. Transactions
	1. Debit 
	2. Credit transaction
	   
4. Notifications
	1. Send email for account creation
	2. Send debit / credit alert
	3. Send balance alert
	4. send user transaction location alert
	   
3. Program Flow
1. The program checks if user is an existing customer
	1. If YES
		1. The customer is prompted to enter account ID
		2. Select service from list (Deposit, Withdrawal, Check Balance, Get Transaction History, Make Transfer)
		3. The program continues based on user's above preference 
		   
	2. If NO
		1. User is asked to create new account 
			1. If YES
				1. The program continues to create customer section
			2. If NO
				1. Exit the program
				   
2. Registering new customer
	1. The program takes the customer necessary data
	2. Validates the data
	3. Create the new customer
	4. Create the customer account 
	5. Sends notification to the customer
	   
3. Deposit
	1. The customer enters the depositing amount
	2. The value is validated
	3. The transaction is completed
	4. Deposit notification is sent to the customer
	   
4. Withdrawal 
	1. The customer enters the depositing amount
	2. The value is validated
	3. The program checks if the customer has enough balance to perform the transaction
		1. if YES
			1. The program performs the debit transaction and proceeds to the final step
		2. If NO
			1. The withdrawal process exits and the program returns to the main menu
	4. Withdrawal notification is sent to the customer
	   
5. Checking Balance
	1. The program request if the customer wants a copy of the balance sent via email
		1. If YES
			1. The program sends balance notification
			2. The program proceeds to step 2
		2. If NO
			1. The program proceeds to step 2
	2. The program gets the customer balance 
	3. Displays it to the customer
	   
6. Get Transaction History
	1. The customer select what format to receive the transactions (email, display on screen, csv, and pdf)
	2. The program gets the history and sends
	3. The program delivers the history based on the customers choice in step 1

7. Make Transfer
	1. The customer enters the transfer details (Amount, receiver account details)
	2. The program checks if the customer has enough balance to proceed with transfer
		1. If YES
			1. The program debits the customer account
			2. The program credits the recipient accounts 
			3. The program sends a notification to both the sender and the receiver 
		2. If NO
			1. The program sends a not enough balance message on screen and exits the process