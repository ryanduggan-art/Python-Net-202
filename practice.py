# Write your code here :-)
print("Welcome! Please enter customer information.")

first_name = input("First Name: ")
last_name = input("Last Name: " )
while True:
    email = input("Email Address: ")
    if "@" in email and "." in email:
        break
    print("Please enter a valid email address.")
phone = input("Phone Number: ")
address = input("Mailing Address: ")
city = input("City: ")
state = input("State: ")
zip_code = input("Zip Code: ")


# Store the information in a dictionairy
customer = {
    "First Name": first_name,
    "Last Name": last_name,
    "Email": email,
    "Phone": phone,
    "City": city,
    "State": state,
    "Zip Code": zip_code
}


# Print a summary
print("\nCustomer Information Summary:")
print("-------------------------------------")
for key, value in customer.items():
    print(f"{key}: {value}")

customers = []

while True:
    # collect info like before....
    customer = {
    "First Name": first_name,
    "Last Name": last_name,
    "Email": email,
    "Phone": phone,
    "City": city,
    "State": state,
    "Zip Code": zip_code
}
    customers.append(customer)

    cont = input("Add another? (yes/no): ").lower()
    if cont != "yes":
        break


