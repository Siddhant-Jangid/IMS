import add_items
import remove_items
import search_items 
import view_inventory

def display_menu():
    cont = """==================== Inventory Management System ====================
1. View All Items.
2. Search for an Item.
3. Add a New Item.
4. Update an Item.
5. Remove an Item.
6. Exit.
=====================================================================
Enter your choice: """
    print(cont)

while True:
    display_menu()
    choice = input("")
    match choice:
        case "1":
            print("Viewing all items...\n")
            view_inventory.view_inventory()
            print("\n\n")
        case "2":
            print("Choose from below...\n")
            print("1.Search by ID.\n2.Search by Name.\n")
            s_choice = input("")
            if (s_choice=="1"):
                search_items.search_item_by_id()
            elif(s_choice=="2"):
                search_items.search_item_by_name()
            else:
                print("Choose wisely..")
        case "3":
            print("Enter the details to add item: \n")
            add_items.add_item()
            print("Item added successfully..\n\n")
        case "4":
            print("Updating an item...")
            remove_items.remove_item()
            print("Now enter updated details: \n")
            add_items.add_item()
            print("Item successfully updated..\n\n")
        case "5":
            print("Enter the id of the item to remove: \n")
            remove_items.remove_item()
            print("Item removed successfully..\n\n")
        case "6":
            print("Exiting the program...")
            break
        case _:
            print("Invalid choice. Please try again.")

