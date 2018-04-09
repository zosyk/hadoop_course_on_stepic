import re

class CheckBook:
    __original_balance = 0
    __items = []

    def __init__(self, original_balance: float, items):
        self.__original_balance = float(original_balance)
        self.__items = items

    def get_original_balance(self):
        return self.__original_balance

    def get_items(self):
        return self.__items



class CheckBookPrinter:
    """
    Original_Balance:_1000.00
    125_Market_125.45_Balance_874.55
    126_Hardware_34.95_Balance_839.60
    127_Video_7.45_Balance_832.15
    128_Book_14.32_Balance_817.83
    129_Gasoline_16.10_Balance_801.73
    Total_expense__198.27
    Average_expense__39.65
    """

    __check_book = None

    def __init__(self, check_book:CheckBook):
        self.__check_book = check_book


    def print(self):
        result = ""
        book = self.__check_book
        items = book.get_items()

        result += "Original Balance: {:.2f}\r\n".format(book.get_original_balance())

        current_balance = float(book.get_original_balance())
        total_expense = 0
        for item in items:
            current_balance = current_balance - item.get_check_amount()
            total_expense += item.get_check_amount()
            result += "{} {} {:.2f} Balance {:.2f}\r\n".format(item.get_check_number(), item.get_category(), item.get_check_amount(), current_balance)

        result += "Total expense  {:.2f}\r\n".format(total_expense)
        result += "Average expense  {:.2f}".format(total_expense/len(items))


        return result




class Item:
    __check_number = 0
    __category = ''
    __check_amount = 0.0

    def __init__(self, check_number:int, category, check_amount:float):
        self.__check_number = check_number
        self.__category = category
        self.__check_amount = check_amount

    def get_check_number(self):
        return self.__check_number

    def get_category(self):
        return self.__category

    def get_check_amount(self):
        return self.__check_amount

    def __str__(self):
        return "check_number: {}, category: {}, check_amount: {}".format(self.__check_number, self.__category,
                                                                         self.__check_amount)

    def __repr__(self):
        return self.__str__()


class CheckBookParser:

    def parse(self, book):
        splitted_check_book = book.split(" ")
        original_balance = splitted_check_book[0]

        splitted_check_book = splitted_check_book[1:len(splitted_check_book)]


        print(splitted_check_book)
        items = []

        for i in range(int(len(splitted_check_book) / 3)):

            item = Item(splitted_check_book[i*3], splitted_check_book[i*3 + 1], float(splitted_check_book[i*3 + 2]))

            items.append(item)

        return CheckBook(original_balance, items)


b1 = """1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""


def balance(book: str):
    filtered_book = re.sub("\n", " ", re.sub("(?![\w. ]).", "", book)).strip()
    filtered_book = re.sub("  ", " ", filtered_book)

    parser = CheckBookParser

    check_book = parser.parse(parser, filtered_book)

    printer = CheckBookPrinter(check_book)

    return printer.print()




# balance(b1)



