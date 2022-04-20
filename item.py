# Marco Stevanella - 101307949
from __future__ import annotations
from NoInputException import NoInputException


class Item:
    def __init__(self, item_list: list[Item]):
        self.code: int = Item.ask_for_item_code(item_list)
        self.name: str = Item.ask_for_item_name()
        self.cost: float = Item.ask_for_item_cost()

    def __str__(self):
        return f"{self.code}\t|\t{self.name}\t|\t{self.cost}"

    HEADERS = {
        'ITEM_CODE': "Code",
        'ITEM_NAME': "Name",
        'ITEM_COST': "Price",
    }

    # ask for Item Code - Must be Int and Unique
    @staticmethod
    def ask_for_item_code(items: list[Item]) -> int:
        while True:
            item_code = input("Enter the Item Code: ")
            if item_code == 'No':
                raise NoInputException
            if not item_code.isnumeric():
                print("Item Code Must be numeric")
                continue
            item_code = int(item_code)
            is_unique = True
            for item in items:
                if item.code == item_code:
                    print("This Item Code already belongs to " + item.name + ". Try a new code")
                    is_unique = False
                    break
            if is_unique:
                return item_code

    # ask for Item Name - Must be a str
    @staticmethod
    def ask_for_item_name() -> str:
        while True:
            name = input('Enter item name: ')
            if name == 'No':
                raise NoInputException()
            if name.replace(' ', '').isalpha():
                return name
            print("Invalid input: Must contain letters only")

    # ask for Item Cost - Must be a float fixed to 2 decimal points
    @staticmethod
    def ask_for_item_cost() -> float:
        while True:
            price = input("Enter Item price: ")
            if price == 'No':
                raise NoInputException()
            if price.replace('.', '').isnumeric():
                price = float(price)
                return price
            else:
                print("Price must be a number")
                continue

    @staticmethod
    def display_items_summary(items: list[Item]) -> None:
        separator = '  |   '
        max_length_item_code_header = max([len(str(i.code)) for i in items] + [len(Item.HEADERS['ITEM_CODE'])])
        max_length_item_name_header = max([len(str(i.name)) for i in items] + [len(Item.HEADERS['ITEM_NAME'])])
        max_length_item_cost_header = max([len(str(i.cost)) for i in items] + [len(Item.HEADERS['ITEM_COST'])])

        paddings = ' ' * (max_length_item_code_header - len(Item.HEADERS['ITEM_CODE']))
        print(f"| {Item.HEADERS['ITEM_CODE'] + paddings + separator}", end='')
        paddings = ' ' * (max_length_item_name_header - len(Item.HEADERS['ITEM_NAME']))
        print(f"{Item.HEADERS['ITEM_NAME'] + paddings + separator}", end='')
        paddings = ' ' * (max_length_item_cost_header - len(Item.HEADERS['ITEM_COST']))
        print(f"{Item.HEADERS['ITEM_COST'] + paddings + separator}")

        for item in items:
            print("| ", end='')
            # COLUMN: CODE
            paddings = ' ' * (max_length_item_code_header - len(str(item.code)))
            print(f"{str(item.code) + paddings + separator}", end='')
            # COLUMN: NAME
            paddings = ' ' * (max_length_item_name_header - len(str(item.name)))
            print(f"{str(item.name) + paddings + separator}", end='')
            # COLUMN: COST
            paddings = ' ' * (max_length_item_cost_header - len(str(item.cost)))
            print(f"{str(item.cost) + paddings + separator}")

