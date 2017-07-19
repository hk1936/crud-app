import os

print("----------------------------")
print("Products Application")
print("----------------------------")

menu = """
Hello,

Welcome to the product app!

There are 100 products.

Please choose an operation from:'List', 'Show', 'Create', 'Update', 'Destroy'
"""
print (menu)
chosen_operation = input()

if chosen_operation.title() == "List": #.title() if list is small letter, it will still capture
    print ("Listing products")
elif chosen_operation.title() == "Show":
    print ("Showing A product")
elif chosen_operation.title() == "Create":
    print ("Creating A product")
elif chosen_operation.title() == "Update":
    print ("Updating A product")
elif chosen_operation.title() == "Destroy":
    print ("Destroying A product")
else:
    print("Operation not recognized. Choose appropriate operation from:'List', 'Show', 'Create', 'Update', 'Destroy'!")
