class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit number.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if str(phone) != phone_number]

    def edit_phone(self, old_phone_number, new_phone_number):
        for phone in self.phones:
            if str(phone) == old_phone_number:
                phone.value = new_phone_number

    def find_phone(self, phone_number):
        return next((phone for phone in self.phones if str(phone) == phone_number), None)

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}"

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        self.data.pop(name, None)

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for record in book.data.values():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")
book.delete("Jane")