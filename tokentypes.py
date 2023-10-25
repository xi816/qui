from dataclasses import dataclass
from typing import Any

class String:
    def __init__(self, s = ""):
        self.cont = [ord(i) for i in s]

    def len(self):
        return len(self.cont)

    def add(self, s):
        self.cont += s

    def pop(self):
        self.cont.pop()

    def acstr(self):
        return "".join(self.cont)

class Token:
    def __init__(self, type, value = ""):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token {self.type} {self.value}"
