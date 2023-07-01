from typing import Any, Callable, List
from collections import UserDict


class Field:
    def __init__(self, value: str):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: str, phones: List[str]):
        self.name = Name(value=name)
        self.phones = []
        for phone in phones:
            self.phones.append(Phone(value=phone))


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

