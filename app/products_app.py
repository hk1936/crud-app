import os
import csv

products =[] #create new lists
csv_file_path = "/users/kawanishihajime/desktop/crud-app/data/products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

print("----------------------------")
print("Products Application")
print("----------------------------")
print("Hello "+os.getlogin())
menu = """
Welcome to the product app!

There are {0} products.

Please choose an operation from:'List', 'Show', 'Create', 'Update', 'Destroy'

When you are DONE, type in DONE!
""".format(len(products))

print (menu)


def list_products():
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row["id"],row["name"],row["aisle"],row["department"], row["price"])



def show_product():
    print("Showing a product")

def create_product():
    print("Creating a product")

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
