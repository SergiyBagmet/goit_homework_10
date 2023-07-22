from collections import UserDict


class Filed:
    def __init__(self, value: str) -> None:
        self.value = value


class Name(Filed):
    def __init__(self, value: str) -> None:
        super().__init__(value)

class Phone(Filed):
    def __init__(self, value: str) -> None:
        if value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Phone must be only str(numbers).")    


class Record:
    def __init__(self, name: Name, *phones: list[Phone]) -> None:
        self.name = name
        self.phones = list(phones)

    def add_phone(self, phone: Phone):   
        self.phones.append(phone)

    def remove_phone(self, phone: Phone):
        self.phones.remove(phone)

    def change_phone(self, old_phone: Phone, new_phone : Phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)
         
    
class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, rec: Record):
        if not isinstance(rec, Record):
            raise ValueError("Record must be an instance of the Record class.")
        self.data[rec.name.value] = rec


if __name__ == '__main__':

    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print('All Ok)')        







