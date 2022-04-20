class Menu:
    EXIT = 'Exit'
    CREATE_EMPLOYEE = 'Create Employee'
    CREATE_ITEM = 'Create Item'
    MAKE_PURCHASE = 'Make Purchase'
    ALL_EMPLOYEES_SUMMARY = 'All Employee Summary'

    menu = {
        1: CREATE_EMPLOYEE,
        2: CREATE_ITEM,
        3: MAKE_PURCHASE,
        4: ALL_EMPLOYEES_SUMMARY,
        5: EXIT,
    }

    @staticmethod
    def print_menu() -> None:
        longest_desc = max([len(desc) for desc in Menu.menu.values()])
        dashes = '-' * (longest_desc + 12)
        print(dashes)
        for key in Menu.menu:
            spaces = ' ' * (longest_desc - len(Menu.menu[key]))
            print(f"|   {key} - {Menu.menu[key] + spaces}   |")
        print(dashes)

    @staticmethod
    def get_menu_keys() -> list:
        return list(Menu.menu.keys())

    @staticmethod
    def ask_for_menu_option() -> int:
        while True:
            # ask for user input
            selection = input("Please select Menu option: ")
            # check user input is a number (when not valid continue to next iteration)
            if not selection.isnumeric():
                print(f"Selection must be a number {Menu.get_menu_keys()}")
                continue
            # check user input is in the menu (when not valid continue to next iteration)
            selection = int(selection)
            if selection not in Menu.menu:
                print(f"Selection must be a valid option {Menu.get_menu_keys()}")
                continue

            # return the valid option
            return selection
