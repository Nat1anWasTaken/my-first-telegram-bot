import random


class NoOptionsInData(Exception):
    pass


class OptionManager:
    def __init__(self):
        self.data: [int, list[str]] = {}

    def add(self, user_id: int, option: str) -> None:
        if user_id not in self.data:
            self.data[user_id] = []

        self.data[user_id].append(option)

    def list(self, user_id: int) -> list[str]:
        if user_id not in self.data:
            return []

        return self.data[user_id]

    def eat(self, user_id: int) -> str:
        if user_id not in self.data:
            raise NoOptionsInData("No options in data")

        return random.choice(self.data[user_id])

    def remove(self, user_id: int, index: int) -> str:
        if user_id not in self.data:
            self.data[user_id] = []

        food = self.data[user_id].pop(index)

        if len(self.data[user_id]) == 0:
            del self.data[user_id]

        return food

    def clear(self, user_id: int):
        if user_id not in self.data:
            return

        del self.data[user_id]
