class User:
    def __init__(self, name: str, user_id: int, user_level: int):
        self.name = name
        self.user_id = user_id
        self.user_level = user_level

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self):
        return hash((self.name, self.user_id))

    def __str__(self):
        return f'name: {self.name}, id: {self.user_id}, level: {self.user_level}'
