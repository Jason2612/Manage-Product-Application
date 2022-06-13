

items_db = {
    1:"Box",
    2:"Bed",
    3:"Chair",
    4:"Television",
    5:"Cup",
}


def get_item_db(items_db, item_id):
    if item_id in items_db:
        print("You got 1 item with this ID: ")
        print(items_db[item_id])

def update_item_db(items_db, item_id, new_item_name):
    if item_id not in items_db:
        items_db[item_id] = new_item_name
    else:
        items_db[item_id] = new_item_name
            

def print_out_menu():
    print('Choose the function you want')
    print('   1. Create new item')
    print('   2. Update name of item with id')
    print('   3. Delete item in list')
    print('   0. Exit')

def input_selection():
    return int(input('Input the number: '))
# print(items_db)
print_out_menu()
option = input_selection()

while option != 0:

    if option == 1:
        product_id = int(input("Type in product id for searching: "))
        if product_id in items_db:
            get_item_db(items_db, product_id)
        else:
            product_name = input("Input product name into the list: ")
            update_item_db(items_db, product_id, product_name)
            print("New item has been updated into the list: ", items_db)

    elif option == 2:
        product_id = int(input("Type in product id for searching: "))
        if product_id in items_db:
            get_item_db(items_db, product_id)
            product_name = input("Input product name into the list: ")
            update_item_db(items_db, product_id, product_name)
            print("New title has update for ID {} with {}".format(product_id,product_name))
            print(items_db)
        else:
            print("This item doesnt't exits")
    
    elif option == 3:
        product_id = int(input("Type in product id for searching: "))
        if product_id in items_db:
            get_item_db(items_db, product_id)
            del items_db[product_id]
            print("The list items after delete", items_db)
        else:
            print("This item doesnt't exits")

    elif option == 0:
        print('Exit')
    else:
        print('Please type again')
    
    print_out_menu()
    option = input_selection()
