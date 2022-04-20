# Marco Stevanella - 101307949
from NoInputException import NoInputException
from menu import Menu
from employee import Employee
from item import Item
from helpers import (
    ask_create_new_employee,
    ask_create_new_item,
    ask_create_new_purchase,
    ask_for_employee_by_discount_code,
    ask_for_item_by_code,
    ask_for_purchase_confirmation,
)

# LISTS
employee_list = []
item_list = []
while True:
    Menu.print_menu()
    user_input = Menu.ask_for_menu_option()
    try:
        if Menu.menu[user_input] == Menu.CREATE_EMPLOYEE:
            while True:
                new_employee = Employee(employee_list)
                employee_list.append(new_employee)
                create_new = ask_create_new_employee()
                if create_new:
                    continue
                else:
                    break
        elif Menu.menu[user_input] == Menu.CREATE_ITEM:
            while True:
                new_item = Item(item_list)
                item_list.append(new_item)
                create_new = ask_create_new_item()
                if create_new:
                    continue
                else:
                    break
        elif Menu.menu[user_input] == Menu.MAKE_PURCHASE:
            # Make Purchase Workflow
            # Step 1
            Item.display_items_summary(item_list)
            while True:
                # Step 2
                employee = ask_for_employee_by_discount_code(employee_list)
                # Step 3
                item = ask_for_item_by_code(item_list)

                # Step 4
                if ask_for_purchase_confirmation():
                    # Step 5
                    employee.make_purchase(item)

                # Step 6
                if ask_create_new_purchase():
                    continue  # make another purchase

                Employee.display_employees_summary(employee_list)
                break  # Go to menu

        elif Menu.menu[user_input] == Menu.ALL_EMPLOYEES_SUMMARY:
            Employee.display_employees_summary(employee_list)

        elif Menu.menu[user_input] == Menu.EXIT:
            break
    except NoInputException:
        continue

print("Goodbye")



