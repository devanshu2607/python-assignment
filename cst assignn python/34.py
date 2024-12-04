def display_inventory(inventory):
    """Displays the current inventory."""
    if not inventory:
        print("The inventory is empty.")
    else:
        print("\nInventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

def add_item(inventory):
    """Adds a new item to the inventory or updates the quantity if it already exists."""
    item = input("Enter the item name to add: ")
    try:
        quantity = int(input(f"Enter the quantity of {item}: "))
        if quantity <= 0:
            print("Quantity must be a positive integer.")
            return
        
        if item in inventory:
            inventory[item] += quantity
            print(f"Updated {item} quantity to {inventory[item]}.")
        else:
            inventory[item] = quantity
            print(f"Added {item} with quantity {quantity}.")
    
    except ValueError:
        print("Error: Please enter a valid number for quantity.")

def remove_item(inventory):
    """Removes an item from the inventory."""
    item = input("Enter the item name to remove: ")
    
    if item in inventory:
        try:
            quantity = int(input(f"Enter the quantity of {item} to remove: "))
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                return
            if quantity > inventory[item]:
                print("Error: Cannot remove more than the available quantity.")
                return
            inventory[item] -= quantity
            
            if inventory[item] == 0:
                del inventory[item]
                print(f"{item} has been removed from the inventory.")
            else:
                print(f"Updated {item} quantity to {inventory[item]}.")
        
        except ValueError:
            print("Error: Please enter a valid number for quantity.")
    else:
        print(f"{item} not found in inventory.")

def main():
    """Main function to manage the inventory system."""
    inventory = {}
    
    while True:
        print("\n-- Inventory System --")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            add_item(inventory)
        elif choice == '3':
            remove_item(inventory)
        elif choice == '4':
            print("Exiting the inventory system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
