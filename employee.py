# Marco Stevanella - 101307949

from __future__ import annotations
from NoInputException import NoInputException
from item import Item


class Employee:
    HEADERS = {
        'EMPLOYEE_ID': "EmployeeID",
        'EMPLOYEE_NAME': "Employee Name",
        'EMPLOYEE_TYPE': "Employee Type",
        'YEARS_WORKED': "Years worked",
        'TOTAL_PURCHASE': "Total Purchased",
        'TOTAL_DISCOUNT': "Total Discount",
        'DISCOUNT_CODE': "Discount Code",
    }

    def __init__(self, employee_list: list[Employee]):

        self.id: int = Employee.ask_for_id(employee_list)
        self.name: str = Employee.ask_for_name()
        self.type: str = Employee.ask_for_employee_type()
        self.years_worked: int = Employee.ask_for_year_worked()
        self.discount_code: int = Employee.ask_for_discount_code(employee_list)
        self.total_purchased: float = 0
        self.total_discount: float = 0

    def make_purchase(self, item: Item) -> None:
        if self.total_discount <= 200:
            year_rate = 2
            # discount at 2% each year worked, max 10%
            total_discount_percent = min(year_rate * self.years_worked, 10)
            # managers get + 10%
            if self.type.lower() == 'manager':
                total_discount_percent += 10
            elif self.type.lower() == 'hourly':
                total_discount_percent += 2

            discount_amount = round(item.cost * total_discount_percent / 100, 2)
            purchase_amount = round(item.cost - discount_amount, 2)
            self.total_purchased += purchase_amount
            self.total_discount += discount_amount

        else:
            selection = input("$200 Limit reached: Would you like to buy it anyway? say yes or no").lower()
            if selection == 'yes':
                self.total_purchased += item.cost

    @staticmethod
    def ask_for_id(employees: list[Employee]) -> int:
        # Input id
        # Must be a number
        while True:
            employee_id = input("Please give the Employee Id: ").lower()
            if employee_id == 'no':
                raise NoInputException()
            if not employee_id.isnumeric():
                print("ID must ne numeric")
                continue
            employee_id = int(employee_id)
            # check for uniqueness
            is_unique = True
            for employee in employees:
                if employee.id == employee_id:
                    print("This ID is already been taken, try a new one")
                    is_unique = False
                    break
            if is_unique:
                return employee_id

    @staticmethod
    def ask_for_year_worked() -> int:
        while True:
            years_worked = input('Enter employee years worked: ').lower()
            if years_worked == 'no':
                raise NoInputException()
            if years_worked.isnumeric():
                return int(years_worked)
            print("Invalid input.")

    @staticmethod
    def ask_for_discount_code(employees: list[Employee]) -> int:
        while True:
            code = input('Enter employee discount code: ').lower()
            if code == 'No':
                raise NoInputException()
            if not code.isnumeric():
                print("Discount Code must be numeric")
                continue
            code = int(code)
            # Check for uniqueness
            is_unique = True
            for employee in employees:
                if employee.discount_code == code:
                    print("Discount Code is already been taken, try a new one")
                    is_unique = False
                    break
            if is_unique:
                return code

    @staticmethod
    def ask_for_employee_type() -> str:
        while True:
            employee_type = input('Enter employee type (Manager or Hourly): ').lower()
            if employee_type == 'no':
                raise NoInputException()
            if employee_type in ['manager', 'hourly']:
                return employee_type
            print("Invalid input.")

    @staticmethod
    def ask_for_name() -> str:
        while True:
            name = input('Enter name: ').lower()
            if name == 'no':
                raise NoInputException()
            if name.replace(' ', '').isalpha():
                return name
            print("Invalid input: Must contain alphabetic characters only")

    @staticmethod
    def display_employees_summary(employees: list[Employee]) -> None:
        separator = '  |   '
        # find the lengths of each column
        max_length_employee_id_header = max([len(str(e.id)) for e in employees] + [len(Employee.HEADERS['EMPLOYEE_ID'])])
        max_length_employee_name_header = max([len(e.name) for e in employees] + [len(Employee.HEADERS['EMPLOYEE_NAME'])])
        max_length_employee_type_header = max([len(e.type) for e in employees] + [len(Employee.HEADERS['EMPLOYEE_TYPE'])])
        max_length_employee_years_worked_header = max([len(str(e.years_worked)) for e in employees] + [len(Employee.HEADERS['YEARS_WORKED'])])
        max_length_employee_tot_purchased_header = max([len(str(e.total_purchased)) for e in employees] + [len(Employee.HEADERS['TOTAL_PURCHASE'])])
        max_length_employee_tot_discount_header = max([len(str(e.total_discount)) for e in employees] + [len(Employee.HEADERS['TOTAL_DISCOUNT'])])
        max_length_employee_discount_code_header = max([len(str(e.discount_code)) for e in employees] + [len(Employee.HEADERS['DISCOUNT_CODE'])])

        # print the headers
        paddings = ' ' * (max_length_employee_id_header - len(Employee.HEADERS['EMPLOYEE_ID']))
        print(f"| {Employee.HEADERS['EMPLOYEE_ID'] + paddings + separator}", end='')
        paddings = ' ' * (max_length_employee_name_header - len(Employee.HEADERS['EMPLOYEE_NAME']))
        print(f"{Employee.HEADERS['EMPLOYEE_NAME'] + paddings + separator}", end='')
        paddings = ' ' * (max_length_employee_type_header - len(Employee.HEADERS['EMPLOYEE_TYPE']))
        print(f"{Employee.HEADERS['EMPLOYEE_TYPE'] + paddings + separator}", end='')
        paddings = ' ' * (max_length_employee_years_worked_header - len(Employee.HEADERS['YEARS_WORKED']))
        print(f"{Employee.HEADERS['YEARS_WORKED'] + paddings + separator}", end='')
        paddings = ' ' * (max_length_employee_tot_purchased_header - len(Employee.HEADERS['TOTAL_PURCHASE']))
        print(f"{Employee.HEADERS['TOTAL_PURCHASE'] + paddings + separator}", end='')
        paddings = ' ' * (max_length_employee_tot_discount_header - len(Employee.HEADERS['TOTAL_DISCOUNT']))
        print(f"{Employee.HEADERS['TOTAL_DISCOUNT'] + paddings + separator}", end='')
        paddings = ' ' * (max_length_employee_discount_code_header - len(Employee.HEADERS['DISCOUNT_CODE']))
        print(f"{Employee.HEADERS['DISCOUNT_CODE'] + paddings + separator}")

        # print each employee row
        for employee in employees:
            print("| ", end='')
            # COLUMN: ID
            paddings = ' ' * (max_length_employee_id_header - len(str(employee.id)))
            print(f"{str(employee.id) + paddings + separator}", end='')

            # COLUMN: NAME
            paddings = ' ' * (max_length_employee_name_header - len(employee.name))
            print(f"{employee.name + paddings + separator}", end='')

            # COLUMN: TYPE
            paddings = ' ' * (max_length_employee_type_header - len(employee.type))
            print(f"{employee.type + paddings + separator}", end='')

            # COLUMN: YEARS WORKED
            paddings = ' ' * (max_length_employee_years_worked_header - len(str(employee.years_worked)))
            print(f"{str(employee.years_worked) + paddings + separator}", end='')

            # COLUMN: TOTAL PURCHASED
            paddings = ' ' * (max_length_employee_tot_purchased_header - len(str(employee.total_purchased)))
            print(f"{str(employee.total_purchased) + paddings + separator}", end='')

            # COLUMN: TOTAL DISCOUNT
            paddings = ' ' * (max_length_employee_tot_discount_header - len(str(employee.total_discount)))
            print(f"{str(employee.total_discount) + paddings + separator}", end='')

            # COLUMN: DISCOUNT CODE
            paddings = ' ' * (max_length_employee_discount_code_header - len(str(employee.discount_code)))
            print(f"{str(employee.discount_code) + paddings + separator}")
