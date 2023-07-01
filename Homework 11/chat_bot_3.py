from typing import Any, Callable, List, Dict
from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value: str):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value



class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, new_value):
        new_value = self.sanitize(new_value)
        valid_phone = self.validation(new_value=new_value)
        if valid_phone is not False:
            self.__value = valid_phone

    def validation(self, new_value):
        if len(new_value) == 12:
            new_value = '+' + new_value
        elif len(new_value) == 13:
            pass
        else:
            new_value = '+38' + new_value
        if len(new_value) != 13:
            print('Invalid Phone, try again')
            return False
        return new_value

    def sanitize(self, new_value):
        new_phone = (
            new_value.strip()
                .strip("+")
                .replace("(", "")
                .replace(")", "")
                .replace("-", "")
                .replace(" ", "")
        )
        return new_phone


class Birthday(Field):

    @Field.value.setter
    def value(self, birthday: str):
        format = '%d-%m-%Y'
        try:
            datetime.strptime(birthday, format)
            self.__value = birthday
        except Exception:
            print(f'Invalid format. Right format {format}. Try again.')


class Record:
    def __init__(self, name: str, phones: List[str], birthday: str = None):
        self.name = Name(value=name)
        self.phones = []
        for phone in phones:
            self.phones.append(Phone(value=phone))
        if birthday is not None:
            self.birthday = Birthday(value=birthday)
        else:
            self.birthday = None

    def days_to_birthday(self):
        if self.birthday is not None:
            now = datetime.now()
            birthday_date = datetime.strptime(self.birthday.value,'%d/%m/%Y')

            birthday = datetime(now.year, birthday_date.month, birthday_date.day)
            return (birthday - now.today()).days + 1


class AddressBook(UserDict):
    iterator_n = 3

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def __iter__(self):
        return Iterable(address_book=self.data, n=self.iterator_n)


class Iterable:
    def __init__(self, address_book: Dict, n: int):
        self.current_index = 0
        self.address_book = address_book
        self.n = n

    def __next__(self):
        if self.current_index < len(self.address_book):
            result_dict = {}
            end_index = self.current_index + self.n
            if end_index > len(self.address_book):
                end_index = len(self.address_book)
            keys = list(self.address_book.keys())[self.current_index:end_index]
            for key in keys:
                result_dict[key] = self.address_book[key]
            self.current_index += self.n
            return result_dict
        else:
            raise StopIteration


if __name__ == '__main__':
    rec1 = Record(name="Test", phones=["+3805555555"], birthday='11/11/2022')
    rec2 = Record(name="Test1", phones=["+3805555555"], birthday='11/11/2022')
    rec3 = Record(name="Test2", phones=["+3805555555"], birthday='11/11/2022')
    rec4 = Record(name="Test3", phones=["+3805555555"], birthday='11/11/2022')
    rec5 = Record(name="Test4", phones=["+3805555555"], birthday='11/11/2022')
    rec6 = Record(name="Test5", phones=["+3805555555"], birthday='11/11/2022')
    rec7 = Record(name="Test6", phones=["+3805555555"], birthday='11/11/2022')
    rec8 = Record(name="Test7", phones=["+3805555555"], birthday='11/11/2022')
    ad = AddressBook()
    ad.add_record(rec1)
    ad.add_record(rec2)
    ad.add_record(rec3)
    ad.add_record(rec4)
    ad.add_record(rec5)
    ad.add_record(rec6)
    ad.add_record(rec7)
    ad.add_record(rec8)
    for records in ad:
        print(records)
    print(ad["Test"].days_to_birthday())
