import os
import csv

products =[] #create new lists
csv_file_path = "/users/kawanishihajime/desktop/crud-app/data/products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

example_new_product = {"id": 21,"name":"New Item!", "aisle":"snacks","department":"ok","price": 3.55}
products.append(example_new_product)

other_path = "/users/kawanishihajime/desktop/crud-app/data/other_products.csv"
with open(other_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)



print("----------------------------")
print("Products Application")
print("----------------------------")
print("Hello "+os.getlogin())
menu = """
Welcome to the product app!

There are {0} products.

Please choose an operation from:'List', 'Show', 'Create', 'Update', 'Destroy'

When you are DONE, type in DONE!
""".format(len(products)) #string interporation



print (menu)


def list_products():
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row["id"],row["name"],row["aisle"],row["department"], row["price"])

def show_product():
	product_id = input("Please specify product IDs: ")


def create_product():
    print("Ok, Please specify the product information....")
    product_name = input("name: ")
    product_aisle = input("aisle: ")
    product_department = input("department: ")
    product_price = input("price: ")
    new_product = {
    	"name": product_name,
    	"aisle":product_aisle,
    	"department":product_department,
    	"price":product_price
    }
    print ("New product is", new_product)
    products.append(new_product)

def update_product():
    print("Updating a product")


def destroy_product():
    print("Destroying a product")


while True:
    chosen_operation = input("Enter operation here: ")
    chosen_operation = chosen_operation.title()
    print ("You chose...."+chosen_operation)

    if chosen_operation == "List": #.title() if list is small letter, it will still capture
        list_products()
    elif chosen_operation  == "Show":
        show_product()
    elif chosen_operation == "Create":
        create_product()
    elif chosen_operation == "Update":
        update_product()
    elif chosen_operation == "Destroy":
        destroy_product()
    elif chosen_operation.title() == "Done":
        print ("Good bye!")
        break
    else:
        print("Operation not recognized. Choose appropriate operation from:'List', 'Show', 'Create', 'Update', 'Destroy'!")
