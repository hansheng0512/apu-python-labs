def check_is_code_exist(target_code, target):
    """
    Function to check if supplier/hospital/item code is valid
    :param target_code: supplier code/hospital code/item code
    :param target: HOSPITAL/SUPPLIER/ITEM
    :return: return True if exist, False if not
    """
    if target == "SUPPLIER":
        file_object = open("suppliers.txt", "r")
    elif target == "HOSPITAL":
        file_object = open("hospitals.txt", "r")
    elif target == "ITEM":
        file_object = open("ppe.txt", "r")
    else:
        print("Invalid target")
        return False
    for details in file_object:
        details = details.rstrip()
        details = details.split(",")
        if details[0] == target_code:
            file_object.close()
            return True
    file_object.close()
    return False


def get_input_supplier_code(check_is_exist = False):
    """
    Function to ask valid supplier code input
    :param check_is_exist: boolean, check if supplier code exist
    :return: return supplier code
    """
    supplier_code = input("Enter Supplier Code: ")
    while True:
        if supplier_code == "":
            print("Supplier code cannot be empty")
            supplier_code = input("Enter supplier code: ")
        else:
            if check_is_exist:
                is_valid_supplier = check_is_code_exist(supplier_code, "SUPPLIER")
                if is_valid_supplier:
                    return supplier_code
                else:
                    print("Supplier not found")
                    supplier_code = input("Enter Supplier Code: ")
            else:
                return supplier_code


def get_string_input(title):
    """
    Function to ask valid string input
    :param title: title
    :return: valid input from user
    """
    string_input = input("Enter {}: ".format(title))
    while True:
        if string_input == "":
            print("{} cannot be empty".format(title))
            string_input = input("Enter {}: ".format(title))
        else:
            return string_input


def update_supplier_details():
    """
    This function will update the supplier details
    """
    view_all_supplier()
    supplier_code = get_input_supplier_code()
    supplier_new_name = get_string_input("New Supplier Name")
    supplier_new_address = get_string_input("New Supplier Address")

    initial_supplier_file_object = open("suppliers.txt", "r")
    initial_supplier_file_object_list = []

    for initial_supplier_details in initial_supplier_file_object:
        initial_supplier_details = initial_supplier_details.rstrip()
        initial_supplier_details = initial_supplier_details.split(",")
        if initial_supplier_details[0].lower() == supplier_code.lower():
            supplier_code_to_save = supplier_code
            supplier_name_to_save = supplier_new_name
            supplier_address_to_save = supplier_new_address
        else:
            supplier_code_to_save = initial_supplier_details[0]
            supplier_name_to_save = initial_supplier_details[1]
            supplier_address_to_save = initial_supplier_details[2]
        initial_supplier_file_object_list.append("{},{},{}".format(supplier_code_to_save, supplier_name_to_save,
                                                                   supplier_address_to_save))

    temp_supplier_file_object = open("suppliers.txt", "w")
    for initial_supplier_file_item in initial_supplier_file_object_list:
        temp_supplier_file_object.write(initial_supplier_file_item + "\n")
    # temp_supplier_file_object.write(
    #     "{},{},{}".format(supplier_code, supplier_name_to_save, supplier_address_to_save))
    # temp_supplier_file_object.write("\n")

    initial_supplier_file_object.close()
    temp_supplier_file_object.close()
    print("Profile Updated Successfully")


def sort_and_filter_item_search(supplier_code_list, target_hospital_list, quantity_list, item_code_list):
    """
    This function will sort and filter the item list
    :param supplier_code_list: List of Supplier Code
    :param target_hospital_list:  List of Hospital Code
    :param quantity_list: List of Quantity Code
    :param item_code_list: List if Item Code
    """
    supplier_code_list_to_show = []
    target_hospital_list_to_show = []
    quantity_list_to_show = []
    item_code_list_to_show = []
    while len(supplier_code_list) > 0:
        ref1 = supplier_code_list.pop(0)
        ref2 = target_hospital_list.pop(0)
        ref3 = quantity_list.pop(0)
        ref4 = item_code_list.pop(0)
        j = 0
        while j < len(supplier_code_list):
            data1 = supplier_code_list[j]
            data2 = target_hospital_list[j]
            data3 = quantity_list[j]
            data4 = item_code_list[j]
            if data1.lower() == ref1.lower() and data2.lower() == ref2.lower() and data4.lower() == ref4.lower():
                ref3 += data3
                supplier_code_list.pop(j)
                target_hospital_list.pop(j)
                quantity_list.pop(j)
                item_code_list.pop(j)
                continue
            j += 1
        supplier_code_list_to_show.append(ref1)
        target_hospital_list_to_show.append(ref2)
        quantity_list_to_show.append(ref3)
        item_code_list_to_show.append(ref4)

    print("{:<15} {:<15} {:<15} {:<15}".format("Supplier Code", "Target Hospital", "Quantity", "Item Code"))
    index = 0
    for supplier_code in supplier_code_list_to_show:
        print("{:<15} {:<15} {:<15} {:<15}".format(supplier_code, target_hospital_list_to_show[index],
                                                 quantity_list_to_show[index], item_code_list_to_show[index]))
        index = index + 1


def get_input_item_code(check_is_exist = False, add_item = False):
    """
    Function to ask valid item code input
    :param check_is_exist: boolean, check if item code exist
    :return: return item code
    """
    item_code = input("Enter item code: ")
    while True:
        if item_code == "":
            print("Item code cannot be empty")
            item_code = input("Enter item code: ")
        else:
            if check_is_exist:
                is_valid_item = check_is_code_exist(item_code, "ITEM")
                if is_valid_item:
                    if add_item:
                        print("This item already assigned to another supplier")
                        item_code = input("Enter Item Code: ")
                    else:
                        return item_code
                else:
                    if add_item:
                        return item_code
                    print("Item not found")
                    item_code = input("Enter Item Code: ")

            else:
                return item_code


def retrieve_item_history():
    """
    This function will retrieve the distributed item and display the history
    """
    item_code = get_input_item_code(True)
    distribution_file_object = open("distribution.txt", "r")
    supplier_code_list = []
    target_hospital_list = []
    item_code_list = []
    quantity_list = []
    for distribution_details in distribution_file_object:
        distribution_details = distribution_details.rstrip()
        distribution_details = distribution_details.split(",")
        if distribution_details[2].lower() == item_code.lower():
            supplier_code_list.append(distribution_details[0])
            target_hospital_list.append(distribution_details[1])
            item_code_list.append(distribution_details[2])
            quantity_list.append(int(distribution_details[3]))
    sort_and_filter_item_search(supplier_code_list, target_hospital_list, quantity_list, item_code_list)


def update_stock(supplier_code, item_code, new_quantity, action):
    """
    This function will update the stock of the item based on confition
    :param supplier_code: supplier code
    :param item_code: item code
    :param new_quantity: quantity to be updated
    :param action: MINUS/ADD
    :return:
    """
    initial_ppe_file_object = open("ppe.txt", "r")
    initial_ppe_file_object_list = []
    if action == "MINUS":
        for initial_item_details in initial_ppe_file_object:
            initial_item_details = initial_item_details.rstrip()
            initial_item_details = initial_item_details.split(",")
            if initial_item_details[3].lower() == supplier_code.lower() and initial_item_details[0].lower() == item_code.lower():
                final_quantity = str(int(initial_item_details[2]) - new_quantity)
            else:
                final_quantity = initial_item_details[2]
            initial_ppe_file_object_list.append("{},{},{},{}".format(initial_item_details[0], initial_item_details[1],
                                                                     final_quantity, supplier_code))

        temp_ppe_file_object = open("ppe.txt", "w")
        for initial_ppe_file_item in initial_ppe_file_object_list:
            temp_ppe_file_object.write(initial_ppe_file_item + "\n")

    elif action == "ADD":
        for initial_item_details in initial_ppe_file_object:
            initial_item_details = initial_item_details.rstrip()
            initial_item_details = initial_item_details.split(",")
            if initial_item_details[3].lower() == supplier_code.lower() and initial_item_details[0].lower() == item_code.lower():
                initial_ppe_file_object_list.append("{},{},{},{}".format(initial_item_details[0], initial_item_details[1],
                                      str(int(initial_item_details[2]) + new_quantity), supplier_code))
            else:
                initial_ppe_file_object_list.append(
                    "{},{},{},{}".format(initial_item_details[0], initial_item_details[1], initial_item_details[2],
                                         supplier_code))

        temp_ppe_file_object = open("ppe.txt", "w")
        for initial_ppe_file_item in initial_ppe_file_object_list:
            temp_ppe_file_object.write(initial_ppe_file_item + "\n")
    initial_ppe_file_object.close()
    temp_ppe_file_object.close()
    print("Stock updated successfully")


def check_item_stock_is_enough(supplier_code, item_code, quantity_needed):
    """
    This function will check the stock of the item is enough or not
    :param supplier_code: supplier code
    :param item_code: ttem code
    :param quantity_needed: quantity needed, use to compare with stock in database
    :return:
    """
    ppe_file_object = open("ppe.txt", "r")
    for ppe_details in ppe_file_object:
        ppe_details = ppe_details.rstrip()
        ppe_details = ppe_details.split(",")
        if ppe_details[3] == supplier_code and ppe_details[0] == item_code:
            if int(ppe_details[2]) < int(quantity_needed):
                return False, ppe_details[2]
            else:
                return True, ppe_details[2]
    return False, 0


def get_input_hospital_code(check_is_exist = False):
    """
    Function to ask valid hospital code input
    :param check_is_exist: boolean, check if hospital code exist
    :return: return hospital code
    """
    hospital_code = input("Enter hospital code: ")
    while True:
        if hospital_code == "":
            print("Hospital code cannot be empty")
            hospital_code = input("Enter hospital Code: ")
        else:
            if check_is_exist:
                is_valid_hospital = check_is_code_exist(hospital_code, "HOSPITAL")
                if is_valid_hospital:
                    return hospital_code
                else:
                    print("Hospital not found")
                    hospital_code = input("Enter Hospital Code: ")
            else:
                return hospital_code


def get_number_input(title):
    """
    Function to ask valid number input
    :param title: title
    :return: valid input from user
    """
    number_input = input("Enter {}: ".format(title))
    while True:
        if number_input == "":
            print("{} cannot be empty".format(title))
            number_input = input("Enter {}: ".format(title))
        else:
            try:
                number_input = int(number_input)
                return number_input
            except:
                print("{} must be a number".format(title))
                number_input = input("Enter {}: ".format(title))


def distribution_process():
    """
    This function will process the distribution record and update the stock
    """
    distribution_file_object = open("distribution.txt", "a")
    view_all_supplier()
    supplier_code = get_input_supplier_code(True)
    view_all_hospital()
    target_hospital_code = get_input_hospital_code(True)
    view_all_item_based_on_supplier_id(supplier_code)
    item_code = get_input_item_code(True)
    quantity_to_distribute = get_number_input("Quantity to distribute")
    is_stock_enough, balance = check_item_stock_is_enough(supplier_code, item_code, quantity_to_distribute)
    if is_stock_enough:
        update_stock(supplier_code, item_code, quantity_to_distribute, "MINUS")
        distribution_file_object.write(
            "{},{},{},{}".format(supplier_code, target_hospital_code, item_code, quantity_to_distribute))
        distribution_file_object.write("\n")
    else:
        print("Invalid stock, remaining {} only".format(balance))
    distribution_file_object.close()


def distribution_module():
    """
    This function will process the distribution module
    """
    distribute_item = True
    while distribute_item:
        distribution_process()
        continue_ask_confirm = True
        while continue_ask_confirm:
            break_process = input("Want to distribute next item? [0-no 1-yes]: ")
            if break_process == "0" or break_process == "1":
                if break_process == "0":
                    continue_ask_confirm = False
                    distribute_item = False
                else:
                    continue_ask_confirm = False
                    distribute_item = True
            else:
                continue_ask_confirm = True
                print("Invalid Input, only accept 0 and 1")


def sort_item_list(item_list):
    """
    This function will sort the item list by item code
    :param item_list:
    :return: sorted item_list
    """
    init_list = len(item_list)
    for i in range(0, init_list):
        for j in range(0, init_list - i - 1):
            if item_list[j][0] > item_list[j + 1][0]:
                tempo = item_list[j]
                item_list[j] = item_list[j + 1]
                item_list[j + 1] = tempo
    return item_list


def retrieve_all_based_on_supplier(supplier_code, less_than_threshold = False):
    """
    This function will retrieve all the item based on supplier code
    :param supplier_code: supplier code
    :param less_than_threshold: if True only retrieve the item less than 25, else will retrieve all item
    :return:
    """
    ppe_file_object = open("ppe.txt", "r")
    item_to_show = []
    for ppe_details in ppe_file_object:
        ppe_details = ppe_details.rstrip()
        ppe_details = ppe_details.split(",")
        if ppe_details[3] == supplier_code:
            if less_than_threshold:
                if int(ppe_details[2]) < 25:
                    item_to_show.append(ppe_details)
            else:
                item_to_show.append(ppe_details)
    item_to_show = sort_item_list(item_to_show)
    return item_to_show


def display_item(items_list):
    """
    This function will display the item list
    :param items_list: nested item list
    """
    print()
    print("-" * 50)
    print("View Stocks")
    print("-" * 50)
    print("{:<15} {:<15} {:<15}".format("Item Code", "Item Name", "Quantity"))
    for item in items_list:
        print("{:<15} {:<15} {:<15}".format(item[0], item[1], item[2]))
    print()


def view_stock_less_than_twenty_five():
    """
    This function will view the stock less than 25 based on supplier code
    """
    view_all_supplier()
    supplier_code = get_input_supplier_code(True)
    items_list = retrieve_all_based_on_supplier(supplier_code, True)
    if len(items_list) > 0:
        display_item(items_list)
    else:
        print("No Data")


def view_all_stock():
    """
    This function will view all the stock
    """
    view_all_supplier()
    supplier_code = get_input_supplier_code(True)
    items_list = retrieve_all_based_on_supplier(supplier_code)
    if len(items_list) > 0:
        display_item(items_list)
    else:
        print("No Data")


def add_item(flexible_quantity):
    """
    This function will add the stock to supplier
    :param flexible_quantity: if True, will update the quantity based on the input, else will update the quantity with 100
    """
    supplier_code = get_input_supplier_code(True)
    if flexible_quantity:
        view_all_item_based_on_supplier_id(supplier_code)
        item_code = get_input_item_code(True, False)
        item_quantity = get_number_input("Item Quantity")
        print('Added {} with extra quantity {} to supplier {}'.format(item_code, item_quantity, supplier_code))
        update_stock(supplier_code, item_code, item_quantity, "ADD")
    else:
        item_code = get_input_item_code(True, True)
        item_name = get_string_input("Item Name")
        item_quantity = 100
        print('Added {} with quantity {} to supplier {}'.format(item_code, 100, supplier_code))
        ppe_file_object = open("ppe.txt", "a")
        ppe_file_object.write("{},{},{},{}".format(item_code, item_name, item_quantity, supplier_code))
        ppe_file_object.write("\n")
        ppe_file_object.close()


def inventory_creation(flexible_quantity = False):
    """
    This function will create the assign item to supplier
    :param flexible_quantity: if True, will update the quantity based on the input, else will update the quantity with 100
    """
    if not flexible_quantity:
        file_object = open("ppe.txt", "w")
        file_object.close()
    continue_add_item = True
    while continue_add_item:
        view_all_supplier()
        add_item(flexible_quantity)
        continue_ask_confirm = True
        while continue_ask_confirm:
            break_process = input("Want to add next item? [0-no 1-yes]: ")
            if break_process == "0" or break_process == "1":
                if break_process == "0":
                    continue_ask_confirm = False
                    continue_add_item = False
                else:
                    continue_ask_confirm = False
                    continue_add_item = True
            else:
                continue_ask_confirm = True
                print("Invalid Input, only accept 0 and 1")


def add_supplier(current_supplier):
    """
    Function to add supplier
    :param current_supplier: current supplier
    """
    print("Insert supplier {} details".format(current_supplier))
    supplier_code = get_input_supplier_code()
    while True:
        is_supplier_exist = check_is_code_exist(supplier_code, "SUPPLIER")
        if is_supplier_exist:
            print("Supplier code already exist")
            supplier_code = get_input_supplier_code()
        else:
            break
    supplier_file_object = open("suppliers.txt", "a")
    supplier_name = get_string_input("Supplier name")
    supplier_address = get_string_input("Supplier address")
    supplier_file_object.write("{},{},{}".format(supplier_code, supplier_name, supplier_address))
    supplier_file_object.write("\n")
    supplier_file_object.close()
    print("Supplier {} added successfully\n".format(current_supplier))


def supplier_registration():
    """
    Function to register supplier
    """
    print("Supplier registration")
    print("All previous supplier details will be overwritten")
    min_supplier = 3
    max_supplier = 4
    current_supplier = 1

    # Clear Supplier File
    file_object = open("suppliers.txt", "w")
    file_object.close()

    while current_supplier <= max_supplier:
        add_supplier(current_supplier)
        if current_supplier == min_supplier:
            continue_ask_confirm = True
            while continue_ask_confirm:
                break_process = input("Want to add 4th supplier? [0-no 1-yes]: ")
                if break_process == "0" or break_process == "1":
                    if break_process == "0":
                        continue_ask_confirm = False
                        current_supplier = 5
                    else:
                        continue_ask_confirm = False
                else:
                    continue_ask_confirm = True
                    print("Invalid Input, only accept 0 and 1")
        current_supplier += 1


def add_hospital(current_hospital):
    """
    Function to add hospital
    :param current_hospital: current supplier
    """
    print("Insert hospital {} details".format(current_hospital))
    hospital_code = get_input_hospital_code()
    while True:
        is_hospital_exist = check_is_code_exist(hospital_code, "HOSPITAL")
        if is_hospital_exist:
            print("Hospital code already exist")
            hospital_code = get_input_hospital_code()
        else:
            break
    hospital_file_object = open("hospitals.txt", "a")
    hospital_name = get_string_input("Hospital name")
    hospital_address = get_string_input("Hospital address")
    hospital_file_object.write("{},{},{}".format(hospital_code, hospital_name, hospital_address))
    hospital_file_object.write("\n")
    hospital_file_object.close()
    print("Hospital {} added successfully\n".format(current_hospital))


def hospital_registration():
    """
    Function to register hospital
    """
    print("Hospital registration")
    print("All previous hospital details will be overwritten")
    min_hospital = 3
    max_hospital = 4
    current_hospital = 1

    # Clear Hospital File
    file_object = open("hospitals.txt", "w")
    file_object.close()

    while current_hospital <= max_hospital:
        add_hospital(current_hospital)
        if current_hospital == min_hospital:
            continue_ask_confirm = True
            while continue_ask_confirm:
                break_process = input("Want to add 4th hospital? [0-no 1-yes]: ")
                if break_process == "0" or break_process == "1":
                    if break_process == "0":
                        continue_ask_confirm = False
                        current_hospital = 5
                    else:
                        continue_ask_confirm = False
                else:
                    continue_ask_confirm = True
                    print("Invalid Input, only accept 0 and 1")
        current_hospital += 1


def view_all_supplier():
    """
    Function to view all supplier
    """
    print("View all suppliers")
    file_object = open("suppliers.txt", "r")
    print("-" * 50)
    print("Suppliers List")
    print("-" * 50)
    print("{:<15} {:<15} {:<15}".format("Supplier Code", "Supplier Name", "Supplier Address"))
    for line in file_object:
        line = line.rstrip()
        line = line.split(",")
        print("{:<15} {:<15} {:<15}".format(line[0], line[1], line[2]))
    print("-" * 50)
    file_object.close()


def view_all_hospital():
    """
    Function to view all hospital
    """
    print("View all hospital")
    file_object = open("hospitals.txt", "r")
    print()
    print("-" * 50)
    print("Hospital List")
    print("-" * 50)
    print("{:<15} {:<15} {:<15}".format("Hospital Code", "Hospital Name", "Hospital Address"))
    for line in file_object:
        line = line.rstrip()
        line = line.split(",")
        print("{:<15} {:<15} {:<15}".format(line[0], line[1], line[2]))
    print("-" * 50)
    file_object.close()


def view_all_item_based_on_supplier_id(supplier_code):
    """
    Function to view all item based on supplier id
    """
    print()
    print("-" * 50)
    print("View all item based on supplier id")
    print("-" * 50)
    file_object = open("ppe.txt", "r")
    print("{:<15} {:<15} {:<15}".format("Item Code", "Item Name", "Item Quantity"))
    for line in file_object:
        line = line.rstrip()
        line = line.split(",")
        if line[3] == supplier_code:
            print("{:<15} {:<15} {:<15}".format(line[0], line[1], line[2]))
    file_object.close()


def main_menu():
    """
    Function to display main menu
    """
    while True:
        print("-" * 50)
        print("Inventory System")
        print("-" * 50)
        print("1. Supplier Registration")
        print("2. Hospital Registration")
        print("3. Add New Item for Supplier")
        print("4. View All Stock")
        print("5. View Stock which less than 25")
        print("6. Distribute Item to Hospital")
        print("7. Search Item based on Item Code")
        print("8. Supplier Profile Update")
        print("9. Update Supplier Existing Stock")
        print("10. Exit")
        option = input("Enter Option: ")
        try:
            option = int(option)
            if 1 <= option <= 10:
                if option == 1:
                    supplier_registration()
                elif option == 2:
                    hospital_registration()
                elif option == 3:
                    inventory_creation()
                elif option == 4:
                    view_all_stock()
                elif option == 5:
                    view_stock_less_than_twenty_five()
                elif option == 6:
                    distribution_module()
                elif option == 7:
                    retrieve_item_history()
                elif option == 8:
                    update_supplier_details()
                elif option == 9:
                    inventory_creation(True)
                elif option == 10:
                    print("Bye")
                    break
            else:
                print("Invalid Option")
        except:
            print("Option must be a number")


if __name__ == '__main__':
    main_menu()