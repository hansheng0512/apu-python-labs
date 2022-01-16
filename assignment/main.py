import os


def supplier_login():
    is_valid_supplier = True
    while is_valid_supplier:
        supplier_code = input("Please input supplier code: ")
        if supplier_code != "":
            supplier_file_object = open("supplier.txt", "r")
            for supplier_details in supplier_file_object.readlines():
                supplier_details = supplier_details.rstrip()
                supplier_details = supplier_details.split(",")
                raw_supplier_name = supplier_details[0]
                raw_supplier_code = supplier_details[1].rstrip()
                if supplier_code == raw_supplier_code:
                    print("Supplier Found")
                    return
            print("Invalid Supplier")
            continue_ask_research = True
            while continue_ask_research:
                break_process = input("Want to research? [0-no 1-yes]: ")
                if break_process == "0" or break_process == "1":
                    if break_process == "0":
                        continue_ask_research = False
                        is_valid_supplier = False
                    else:
                        continue_ask_research = False
                else:
                    continue_ask_research = True
                    print("Invalid Input, only accept 0 and 1")


def supplier_registration():
    supplier_file_object = open("supplier.txt", "w")
    min_supplier = 3
    max_supplier = 4
    current_supplier = 1
    while current_supplier <= max_supplier:
        supplier_code = input("Enter Supplier Code: ")
        if supplier_code == "":
            print("Invalid Supplier Code")
            continue
        supplier_name = input("Enter Supplier Name: ")
        if supplier_name == "":
            print("Invalid Supplier Name")
        if supplier_name != "" and supplier_code != "":
            supplier_file_object.write("{},{}".format(supplier_name, supplier_code))
            supplier_file_object.write("\n")
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
    supplier_file_object.close()


def hospital_registration():
    hospital_file_object = open("hospital.txt", "w")
    min_hospital = 3
    max_hospital = 4
    current_hospital = 1
    while current_hospital <= max_hospital:
        hospital_code = input("Enter Hospital Code: ")
        if hospital_code == "":
            print("Invalid Hospital Code")
            continue
        hospital_name = input("Enter Hospital Name: ")
        if hospital_name == "":
            print("Invalid Hospital Name")
        if hospital_name != "" and hospital_code != "":
            hospital_file_object.write("{},{}".format(hospital_name, hospital_code))
            hospital_file_object.write("\n")
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
    hospital_file_object.close()


def initial_inventory_creation():
    ppe_file_object = open("ppe.txt", "w")
    add_item = True
    while add_item:
        supplier_code = input("Enter Supplier Code: ")
        if supplier_code == "":
            print("Invalid Supplier Code")
            continue
        item_code = input("Enter Item Code: ")
        if item_code == "":
            print("Invalid Item Code")
            continue
        if item_code != "" and supplier_code != "":
            ppe_file_object.write("{},{},{}".format(supplier_code, item_code, 100))
            ppe_file_object.write("\n")
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
    ppe_file_object.close()


def add_item_to_inventory():
    ppe_file_object = open("ppe.txt", "a")
    add_item = True
    while add_item:
        supplier_code = input("Enter Supplier Code: ")
        if supplier_code == "":
            print("Invalid Supplier Code")
            continue
        item_code = input("Enter New Item Code: ")
        if item_code == "":
            print("Invalid Item Code")
            continue
        item_quantity = input("Enter New Item Quantity: ")
        if item_quantity == "":
            print("Invalid Item Quantity")
            continue
        else:
            quantity_is_string = True
            while quantity_is_string:
                try:
                    item_quantity = int(item_quantity)
                    quantity_is_string = False
                except:
                    print("Item Quantity must be a number")
                    item_quantity = input("Enter New Item Quantity: ")

        if item_code != "" and supplier_code != "" and item_quantity != "":
            ppe_file_object.write("{},{},{}".format(supplier_code, item_code, item_quantity))
            ppe_file_object.write("\n")
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
    ppe_file_object.close()


def update_item_quantity():
    initial_item_list = []
    initial_ppe_file_object = open("ppe.txt", "r")
    temp_ppe_file_object = open("temp_ppe.txt", "w")
    update_item = True

    for initial_item_details in initial_ppe_file_object:
        initial_item_details = initial_item_details.rstrip()
        initial_item_details = initial_item_details.split(",")
        initial_item_list.append({
            "supplier_code": initial_item_details[0],
            "item_code": initial_item_details[1],
            "item_quantity": initial_item_details[2]
        })
    initial_ppe_file_object.close()

    while update_item:
        edited_item_list = []
        supplier_code = input("Enter Supplier Code: ")
        if supplier_code == "":
            print("Invalid Supplier Code")
            continue
        item_code = input("Enter Item Code: ")
        if item_code == "":
            print("Invalid Item Code")
            continue
        is_item_found = False
        for initial_item_details in initial_item_list:
            if initial_item_details["supplier_code"] == supplier_code and initial_item_details["item_code"] == item_code:
                is_item_found = True
                break
        if not is_item_found:
            print("Invalid Supplier Code or Item Code")
            continue
        item_quantity = input("Enter New Item Quantity: ")
        if item_quantity == "":
            print("Invalid Item Quantity")
            continue
        else:
            quantity_is_string = True
            while quantity_is_string:
                try:
                    item_quantity = int(item_quantity)
                    quantity_is_string = False
                except:
                    print("Item Quantity must be a number")
                    item_quantity = input("Enter New Item Quantity: ")
        if item_code != "" and supplier_code != "" and item_quantity != "" and not quantity_is_string:
            for initial_item_details in initial_item_list:
                if initial_item_details["supplier_code"] == supplier_code and initial_item_details["item_code"] == item_code:
                    edited_item_list.append({
                        "supplier_code": supplier_code,
                        "item_code": item_code,
                        "item_quantity": item_quantity
                    })
                else:
                    edited_item_list.append({
                        "supplier_code": initial_item_details["supplier_code"],
                        "item_code": initial_item_details["item_code"],
                        "item_quantity": initial_item_details["item_quantity"]
                    })
        continue_ask_confirm = True
        while continue_ask_confirm:
            break_process = input("Want to edit next item? [0-no 1-yes]: ")
            if break_process == "0" or break_process == "1":
                if break_process == "0":
                    continue_ask_confirm = False
                    update_item = False
                else:
                    continue_ask_confirm = False
                    update_item = True
            else:
                continue_ask_confirm = True
                print("Invalid Input, only accept 0 and 1")
    for edited_item_details in edited_item_list:
        temp_ppe_file_object.write("{},{},{}".format(edited_item_details["supplier_code"], edited_item_details["item_code"], edited_item_details["item_quantity"]))
        temp_ppe_file_object.write("\n")
    temp_ppe_file_object.close()
    os.rename("temp_ppe.txt", "ppe.txt")


# def distribution_module():



if __name__ == "__main__":
    hospital_registration()
    # update_item_quantity()
    # add_item_to_inventory()
    # supplier_login()
    # supplier_registration()
    # initial_inventory_creation()
