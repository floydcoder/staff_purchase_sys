from __future__ import annotations
from employee import Employee
from item import Item
from NoInputException import NoInputException


def ask_create_new_employee() -> bool:
    create_new_emp = input("press 'Enter' for creating new Employee or any other key to go back to Menu")
    if create_new_emp == "":
        return True
    else:
        return False


def ask_create_new_item() -> bool:
    create_new_item = input("press 'Enter' for creating new Item or any other key to go back to Menu")
    if create_new_item == "":
        return True
    else:
        return False


def ask_create_new_purchase() -> bool:
    create_new_purchase = input("press 'Enter' for creating new purchase or any other key to go back to Menu").lower()
    return create_new_purchase == ""


def ask_for_employee_by_discount_code(employees: list[Employee]) -> Employee:
    while True:
        code = input("Discount Code: ").lower()
        if code == 'no':
            raise NoInputException()
        if not code.isnumeric():
            print("Discount code must be numeric")
            continue
        code = int(code)
        employee = find_employee_by_discount_code(code, employees)
        if employee:
            return employee
        print("Code isn't in use, please double check it or press 'No' to abort")
        continue


def find_employee_by_discount_code(discount_code: int, employees: list[Employee]) -> Employee | None:
    for employee in employees:
        if employee.discount_code == discount_code:
            print("this discount code belongs to employee: " + employee.name)
            return employee
    return None


def ask_for_item_by_code(items: list[Item]) -> Item:
    while True:
        item_code = input("Item ID: ")
        if item_code == 'No' or item_code == 'no':
            raise NoInputException()
        if not item_code.isnumeric():
            print("Item ID must be numeric")
            continue
        item_code = int(item_code)
        item = find_item_by_code(items, item_code)
        if item:
            return item
        print("The item does not exist, please check the ID again or 'No' to abort")
        continue


def ask_for_purchase_confirmation() -> bool:
    selection = input("You want to purchase the item? 'No' to abort, any other key + enter to proceed: ").lower()
    return selection != 'no'


def find_item_by_code(items: list[Item], item_code: int) -> Item | None:
    for item in items:
        if item.code == item_code:
            print("You're about to purchase: " + item.name)
            return item
    return None
