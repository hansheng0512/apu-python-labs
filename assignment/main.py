import datetime
import os


def check_is_supplier_code_valid(supplier_code):
    supplier_file_object = open("supplier.txt", "r")
    for supplier_details in supplier_file_object:
        supplier_details = supplier_details.rstrip()
        supplier_details = supplier_details.split(",")
        if supplier_details[0] == supplier_code:
            return True
    return False


def check_is_hospital_code_valid(hospital_code):
    hospital_file_object = open("hospital.txt", "r")
    for hospital_details in hospital_file_object:
        hospital_details = hospital_details.rstrip()
        hospital_details = hospital_details.split(",")
        if hospital_details[0] == hospital_code:
            return True
    return False


def check_is_item_code_valid(supplier_code, item_code):
    ppe_file_object = open("ppe.txt", "r")
    for ppe_details in ppe_file_object:
        ppe_details = ppe_details.rstrip()
        ppe_details = ppe_details.split(",")
        if ppe_details[0] == supplier_code and ppe_details[1] == item_code:
            return True
    return False


def check_is_item_code_assigned_to_supplier(item_code):
    ppe_file_object = open("ppe.txt", "r")
    for ppe_details in ppe_file_object:
        ppe_details = ppe_details.rstrip()
        ppe_details = ppe_details.split(",")
        if ppe_details[1] == item_code:
            return ppe_details[0]
    return False


def check_item_stock_is_enough(supplier_code, item_code, quantity_needed):
    ppe_file_object = open("ppe.txt", "r")
    for ppe_details in ppe_file_object:
        ppe_details = ppe_details.rstrip()
        ppe_details = ppe_details.split(",")
        if ppe_details[0] == supplier_code and ppe_details[1] == item_code:
            if int(ppe_details[2]) < int(quantity_needed):
                return False, ppe_details[2]
            else:
                return True, ppe_details[2]


def sort_and_filter_item_search(supplier_code_list, target_hospital_list, quantity_list, item_code_list):
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
            if data1 == ref1 and data2 == ref2 and data4 == ref4:
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

    print("{:<15} {:<15} {:<8} {:<8}".format("Supplier Code", "Target Hospital", "Quantity", "Item Code"))
    index = 0
    for supplier_code in supplier_code_list_to_show:
        print("{:<15} {:<15} {:<8} {:<8}".format(supplier_code, target_hospital_list_to_show[index],
                                                 quantity_list_to_show[index], item_code_list_to_show[index]))
        index = index + 1


def update_stock(supplier_code, item_code, new_quantity, action):
    initial_ppe_file_object = open("ppe.txt", "r")
    temp_ppe_file_object = open("temp_ppe.txt", "w")

    if action == "MINUS":
        for initial_item_details in initial_ppe_file_object:
            initial_item_details = initial_item_details.rstrip()
            initial_item_details = initial_item_details.split(",")
            if initial_item_details[0] == supplier_code and initial_item_details[1] == item_code:
                final_quantity = str(int(initial_item_details[2]) - new_quantity)
            else:
                final_quantity = initial_item_details[2]

            temp_ppe_file_object.write(
                "{},{},{}".format(initial_item_details[0], initial_item_details[1], final_quantity))
            temp_ppe_file_object.write("\n")
    elif action == "ADD":
        for initial_item_details in initial_ppe_file_object:
            initial_item_details = initial_item_details.rstrip()
            initial_item_details = initial_item_details.split(",")
            if initial_item_details[0] == supplier_code and initial_item_details[1] == item_code:
                temp_ppe_file_object.write(
                    "{},{},{}".format(initial_item_details[0], initial_item_details[1],
                                      str(int(initial_item_details[2]) + new_quantity)))
            else:
                temp_ppe_file_object.write(
                    "{},{},{}".format(initial_item_details[0], initial_item_details[1], initial_item_details[2]))
            temp_ppe_file_object.write("\n")
    else:
        for initial_item_details in initial_ppe_file_object:
            initial_item_details = initial_item_details.rstrip()
            initial_item_details = initial_item_details.split(",")

            temp_ppe_file_object.write(
                "{},{},{}".format(initial_item_details[0], initial_item_details[1], initial_item_details[2]))
            temp_ppe_file_object.write("\n")
        temp_ppe_file_object.write(
            "{},{},{}".format(supplier_code, item_code, new_quantity))
        temp_ppe_file_object.write("\n")
    initial_ppe_file_object.close()
    temp_ppe_file_object.close()
    os.remove("ppe.txt")
    os.rename("temp_ppe.txt", "ppe.txt")
    print("Stock Updated Successfully")


def supplier_login():
    is_valid_supplier = True
    while is_valid_supplier:
        supplier_code = input("Please input supplier code: ")
        if supplier_code != "":
            supplier_file_object = open("supplier.txt", "r")
            for supplier_details in supplier_file_object.readlines():
                supplier_details = supplier_details.rstrip()
                supplier_details = supplier_details.split(",")
                raw_supplier_name = supplier_details[1]
                raw_supplier_code = supplier_details[0]
                if supplier_code == raw_supplier_code:
                    print("Supplier Found")
                    return supplier_code, raw_supplier_name
            print("Supplier Not Found")
        else:
            print("Supplier Code cannot be empty")


def update_supplier_details(supplier_code):
    supplier_new_name = input("Enter New Supplier Name: ")
    while True:
        if supplier_new_name == "":
            print("Invalid Supplier Name")
            supplier_new_name = input("Enter New Supplier Name: ")
        else:
            break
    supplier_new_address = input("Enter New Supplier Address: ")
    while True:
        if supplier_new_address == "":
            print("Invalid Supplier Address")
            supplier_new_address = input("Enter New Supplier Address: ")
        else:
            break

    initial_supplier_file_object = open("supplier.txt", "r")
    temp_supplier_file_object = open("temp_supplier.txt", "w")

    for initial_supplier_details in initial_supplier_file_object:
        initial_supplier_details = initial_supplier_details.rstrip()
        initial_supplier_details = initial_supplier_details.split(",")
        supplier_code_to_save = supplier_code
        if initial_supplier_details[0] == supplier_code:
            supplier_name_to_save = supplier_new_name
            supplier_address_to_save = supplier_new_address
        else:
            supplier_name_to_save = initial_supplier_details[1]
            supplier_address_to_save = initial_supplier_details[2]
        temp_supplier_file_object.write(
            "{},{},{}".format(supplier_code_to_save, supplier_name_to_save, supplier_address_to_save))
        temp_supplier_file_object.write("\n")

    initial_supplier_file_object.close()
    temp_supplier_file_object.close()
    os.remove("supplier.txt")
    os.rename("temp_supplier.txt", "supplier.txt")
    print("Profile Updated Successfully")


def add_supplier(current_supplier):
    supplier_file_object = open("supplier.txt", "a")
    supplier_code = input("Enter Supplier {} Code: ".format(current_supplier))
    while True:
        if supplier_code == "":
            print("Invalid Supplier Code")
            supplier_code = input("Enter Supplier {} Code: ".format(current_supplier))
        else:
            supplier_is_exist = check_is_supplier_code_valid(supplier_code)
            if supplier_is_exist:
                print("Supplier Code Already Exist")
                supplier_code = input("Enter Supplier {} Code: ".format(current_supplier))
            else:
                break
    supplier_name = input("Enter Supplier {} Name: ".format(current_supplier))
    while True:
        if supplier_name == "":
            print("Invalid Supplier Name")
            supplier_name = input("Enter Supplier {} Name: ".format(current_supplier))
        else:
            break
    supplier_address = input("Enter Supplier {} Address: ".format(current_supplier))
    while True:
        if supplier_name == "":
            print("Invalid Supplier Address")
            supplier_address = input("Enter Supplier {} Address: ".format(current_supplier))
        else:
            break
    supplier_file_object.write("{},{},{}".format(supplier_code, supplier_name, supplier_address))
    supplier_file_object.write("\n")
    supplier_file_object.close()
    print("Supplier {} Added Successfully".format(current_supplier))


def supplier_registration():
    print("Supplier Registration, all old data will be override")
    min_supplier = 3
    max_supplier = 4
    current_supplier = 1
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
    hospital_file_object = open("hospital.txt", "a")
    hospital_code = input("Enter Hospital {} Code: ".format(current_hospital))
    while True:
        if hospital_code == "":
            print("Invalid Hospital Code")
            hospital_code = input("Enter Hospital {} Code: ".format(current_hospital))
        else:
            hospital_is_exist = check_is_hospital_code_valid(hospital_code)
            if hospital_is_exist:
                print("Hospital Code Already Exist")
                hospital_code = input("Enter Hospital {} Code: ".format(current_hospital))
            else:
                break

    hospital_name = input("Enter Hospital {} Name: ".format(current_hospital))
    while True:
        if hospital_name == "":
            print("Invalid Hospital Name")
            hospital_name = input("Enter Hospital {} Name: ".format(current_hospital))
        else:
            break

    hospital_file_object.write("{},{}".format(hospital_code, hospital_name))
    hospital_file_object.write("\n")
    hospital_file_object.close()


def hospital_registration():
    print("Hospital Registration, all old data will be override")
    min_hospital = 3
    max_hospital = 4
    current_hospital = 1
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


def show_supplier_list():
    supplier_file_object = open("supplier.txt", "r")
    print("{:<15} {:<8} {:<8}".format("Supplier Code", "Supplier Name", "Supplier Address"))
    print("-" * 40)
    for supplier_details in supplier_file_object:
        supplier_details = supplier_details.rstrip()
        supplier_details = supplier_details.split(",")
        print("{:<15} {:<8} {:<8}".format(supplier_details[0], supplier_details[1], supplier_details[2]))
    supplier_file_object.close()


def add_item():
    ppe_file_object = open("ppe.txt", "a")
    show_supplier_list()
    supplier_code = input("Which Supplier Code you want to assign to: ")
    while True:
        if supplier_code == "":
            print("Supplier Code cannot be empty")
            supplier_code = input("Enter Supplier Code: ")
        else:
            is_valid_supplier = check_is_supplier_code_valid(supplier_code)
            if is_valid_supplier:
                break
            else:
                print("Invalid Supplier Code")
                supplier_code = input("Enter Supplier Code: ")
    item_code = input("Enter Item Code: ")
    while True:
        if item_code == "":
            print("Item Code cannot be empty")
            item_code = input("Enter Item Code: ")
        else:
            result = check_is_item_code_assigned_to_supplier(item_code)
            if result != False:
                print("This Item already assigned to supplier {}".format(result))
                item_code = input("Enter Item Code: ")
            else:
                break
    item_name = input("Enter Item Name: ")
    while True:
        if item_name == "":
            print("Item Name cannot be empty")
            item_code = input("Enter Item Name: ")
        else:
            break
    ppe_file_object.write("{},{},{}".format(supplier_code, item_code, 100))
    ppe_file_object.write("\n")
    ppe_file_object.close()
    print('Added {} with quantity {} to supplier {}'.format(item_code, 100, supplier_code))


def inventory_creation():
    continue_add_item = True
    while continue_add_item:
        add_item()
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
    print("Initialized Inventory")


def add_item_to_inventory(supplier_code):
    add_item = True
    is_existing_item = False
    while add_item:
        while True:
            if supplier_code == "":
                print("Supplier Code cannot be empty")
                supplier_code = input("Enter Supplier Code: ")
            else:
                is_valid_supplier = check_is_supplier_code_valid(supplier_code)
                if is_valid_supplier:
                    break
                else:
                    print("Invalid Supplier Code")
                    supplier_code = input("Enter Supplier Code: ")

        item_code = input("Enter Item Code: ")
        while True:
            if item_code == "":
                print("Item Code cannot be empty")
                item_code = input("Enter Item Code: ")
            else:
                is_item_exist = check_is_item_code_valid(supplier_code, item_code)
                if is_item_exist:
                    is_existing_item = True
                break

        item_quantity = input("Enter New Item Quantity: ")
        while True:
            if item_quantity == "":
                print("Item Quantity cannot be empty")
                item_quantity = input("Enter New Item Quantity: ")
            else:
                try:
                    item_quantity = int(item_quantity)
                    break
                except:
                    print("Quantity must be a number")
                    item_quantity = input("Enter New Item Quantity: ")

        if is_existing_item:
            update_stock(supplier_code, item_code, item_quantity, "ADD")
        else:
            update_stock(supplier_code, item_code, item_quantity, "NEW")

        continue_ask_confirm = True
        while continue_ask_confirm:
            break_process = input("Want to add next item? [0-no 1-yes]: ")
            if break_process == "0" or break_process == "1":
                if break_process == "0":
                    continue_ask_confirm = False
                    add_item = False
                else:
                    continue_ask_confirm = False
                    add_item = True
            else:
                continue_ask_confirm = True
                print("Invalid Input, only accept 0 and 1")


def distribution_process(supplier_code):
    distribution_file_object = open("distribution.txt", "a")
    while True:
        if supplier_code == "":
            print("Supplier Code cannot be empty")
            supplier_code = input("Enter Supplier Code: ")
        else:
            is_valid_supplier = check_is_supplier_code_valid(supplier_code)
            if is_valid_supplier:
                break
            else:
                print("Supplier not found")
                supplier_code = input("Enter Supplier Code: ")

    target_hospital_code = input("Enter Target Hospital Code: ")
    while True:
        if target_hospital_code == "":
            print("Hospital Code cannot be empty")
            target_hospital_code = input("Enter Target Hospital Code: ")
        else:
            is_valid_hospital_code = check_is_hospital_code_valid(target_hospital_code)
            if is_valid_hospital_code:
                break
            else:
                print("Hospital not found")
                target_hospital_code = input("Enter Target Hospital Code: ")

    item_code = input("Enter Item Code: ")
    while True:
        if item_code == "":
            print("Item Code cannot be empty")
            item_code = input("Enter Item Code: ")
        else:
            is_valid_item = check_is_item_code_valid(supplier_code, item_code)
            if is_valid_item:
                break
            else:
                print("Item not found")
                item_code = input("Enter Item Code: ")

    quantity_to_distribute = input("Enter Quantity to Distribute: ")
    while True:
        if quantity_to_distribute == "":
            print("Quantity cannot be empty")
            quantity_to_distribute = input("Enter Quantity to Distribute: ")
        else:
            try:
                quantity_to_distribute = int(quantity_to_distribute)
                break
            except:
                print("Quantity must be a number")
                quantity_to_distribute = input("Enter Quantity to Distribute: ")

    is_stock_enough, balance = check_item_stock_is_enough(supplier_code, item_code, quantity_to_distribute)
    if is_stock_enough:
        update_stock(supplier_code, item_code, quantity_to_distribute, "MINUS")
        current_timestamp = datetime.datetime.now()
        distribution_file_object.write(
            "{},{},{},{},{}".format(current_timestamp, supplier_code, target_hospital_code, item_code,
                                    quantity_to_distribute))
        distribution_file_object.write("\n")
    else:
        print("Invalid Stock, remaining {} only".format(balance))

    distribution_file_object.close()


def distribution_module(supplier_code):
    distribute_item = True
    while distribute_item:

        distribution_process(supplier_code)

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


def retrieve_all_based_on_supplier(supplier_code):
    ppe_file_object = open("ppe.txt", "r")
    item_to_show = []
    for ppe_details in ppe_file_object:
        ppe_details = ppe_details.rstrip()
        ppe_details = ppe_details.split(",")
        if ppe_details[0] == supplier_code:
            item_to_show.append([ppe_details[0], ppe_details[1], ppe_details[2]])
    return item_to_show


def retrieve_item_history(supplier_code):
    item_code = input("Enter Item Code: ")
    while True:
        if item_code == "":
            print("Item Code cannot be empty")
            item_code = input("Enter Item Code: ")
        else:
            is_valid_item = check_is_item_code_valid(supplier_code, item_code)
            if is_valid_item:
                break
            else:
                print("Item not found")
                item_code = input("Enter Item Code: ")

    distribution_file_object = open("distribution.txt", "r")
    supplier_code_list = []
    target_hospital_list = []
    item_code_list = []
    quantity_list = []
    for distribution_details in distribution_file_object:
        distribution_details = distribution_details.rstrip()
        distribution_details = distribution_details.split(",")
        if distribution_details[1] == supplier_code and distribution_details[3] == item_code:
            supplier_code_list.append(distribution_details[1])
            target_hospital_list.append(distribution_details[2])
            item_code_list.append(distribution_details[3])
            quantity_list.append(int(distribution_details[4]))
    sort_and_filter_item_search(supplier_code_list, target_hospital_list, quantity_list, item_code_list)


def display_item(items_list):
    print("{:<15} {:<8} {:<8}".format("Supplier Code", "Item Code", "Quantity"))
    for item in items_list:
        if int(item[2]) < 25:
            print("{:<15} {:<8} {:<8}".format(item[0], item[1], item[2]))


def supplier_tracking_module():
    supplier_code = input("Enter Supplier Code: ")
    while True:
        if supplier_code == "":
            print("Supplier Code cannot be empty")
            supplier_code = input("Enter Supplier Code: ")
        else:
            is_valid_supplier = check_is_supplier_code_valid(supplier_code)
            if is_valid_supplier:
                break
            else:
                print("Supplier not found")
                supplier_code = input("Enter Supplier Code: ")
    print("Tracking Module")
    print("\t1. View All Stock")
    print("\t2. View Stock which less than 25")
    print("\t3. Search Distributed Item based on Item Id")
    while True:
        option = input("Enter Option: ")
        try:
            option = int(option)
            if option == 1 or option == 2 or option == 3:
                break
            else:
                print("Invalid Option")
        except:
            print("Option must be a number")
    if option == 1:
        items_list = retrieve_all_based_on_supplier(supplier_code)
        if len(items_list) > 0:
            display_item(items_list)
        else:
            print("No Data")
    elif option == 2:
        items_list = retrieve_all_based_on_supplier(supplier_code)
        if len(items_list) > 0:
            display_item(items_list)
        else:
            print("No Data")
    elif option == 3:
        retrieve_item_history(supplier_code)


def supplier_menu(supplier_name, supplier_code):
    print("---Welcome {}, Code: {}---".format(supplier_name, supplier_code))
    print("\t1. Distribute Stock to Hospital")
    print("\t2. Inventory Tracking")
    print("\t3. Profile Update")
    print("\t4. Log Out")
    while True:
        option = input("Enter Option: ")
        try:
            option = int(option)
            if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
                break
            else:
                print("Invalid Option")
        except:
            print("Option must be a number")
    if option == 1:
        distribution_module(supplier_code)
    elif option == 2:
        supplier_tracking_module(supplier_code)
    elif option == 3:
        update_supplier_details(supplier_code)
    elif option == 4:
        print("Thank you, bye")
        exit()


def env_init():
    try:
        os.remove("supplier.txt")
    except:
        pass
    try:
        os.remove("hospital.txt")
    except:
        pass
    try:
        os.remove("ppe.txt")
    except:
        pass
    try:
        os.remove("distribution.txt")
    except:
        pass


if __name__ == "__main__":
    env_init()
    print("---Inventory System---")
    is_first_time = True
    is_logged_in = False
    while True:
        if is_first_time:
            print("First time setup, need to register 3 or 4 suppliers account first and initialize their inventory")
            supplier_registration()
            print("Done supplier registration, next is initialize inventory")
            inventory_creation()
            print("Done inventory creation, 3 or 4 hospital needed to register")
            hospital_registration()
            is_first_time = False
        else:
            print("\t1. Supplier Registration")
            print("\t2. Hospital Registration")
            print("\t3. Supplier Login")
            print("\t4. Assign Item to Supplier")
            print("\t5. Exit")
            while True:
                option = input("Enter Option: ")
                try:
                    option = int(option)
                    if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
                        break
                    else:
                        print("Invalid Option")
                except:
                    print("Option must be a number")
            if option == 1:
                supplier_registration()
            elif option == 2:
                hospital_registration()
            elif option == 3:
                supplier_code, supplier_name = supplier_login()
                supplier_menu(supplier_name, supplier_code)
            elif option == 4:
                inventory_creation()
            elif option == 5:
                print("Thank you, bye")
                exit()
