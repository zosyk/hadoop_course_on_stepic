class Person:
    __name = ''
    __email = ''

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def __str__(self):
        return "{} can be contacted at {}".format(self.__name, self.__email)


person = Person("Brad", "gmail.com")

print(person)


class Customer(Person):
    __balance = 0

    def __init__(self, name, email, balance):
        self.__balance = balance
        self.__name = name
        self.__email = email

        super().__init__(name, email)

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return "{} has a balance {} and can be contacted at {}".format(self.__name, self.__balance, self.__email)


john = Customer("John", "123gmail.com", 10000)

print(john)