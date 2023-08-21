import json
from typing import Set
import os
from sem_14_cw.user_management.user import User
from sem_14_cw.user_management.exceptions import LevelException, AccessException

__all__ = ['Project', 'User', 'LevelException', 'AccessException']


class Project:
    def __init__(self, json_file_path: str):
        self.admin_user = None
        self.json_file_path = json_file_path
        self.users = self.users_from_json()

    def users_from_json(self) -> Set[User]:
        users = set()
        if not os.path.exists(self.json_file_path):
            with open(self.json_file_path, 'w', encoding='utf-8') as empty_file:
                empty_file.write('')
        else:
            with open(self.json_file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            for user in data:
                users.add(User(user['name'], int(user['user_id']), int(user['access_level'])))

        return users

    def dump_users(self):
        with open(self.json_file_path, 'w', encoding='utf-8') as json_file:
            data = [{'name': user.name, 'user_id': user.user_id, 'access_level': user.user_level}
                    for user in self.users]
            json.dump(data, json_file, indent=2, ensure_ascii=False)

    def entrance(self, name: str, user_id: int):
        test_user = User(name, user_id, 0)
        if test_user in self.users:
            for user in self.users:
                if test_user == user:
                    self.admin_user = user
        else:
            raise AccessException(name, user_id)

    def add_user(self, name: str, user_id: int, user_level: int):
        if user_level > self.admin_user.user_level:
            raise LevelException(user_level, self.admin_user)
        new_user = User(name, user_id, user_level)
        self.users.add(new_user)
        self.dump_users()


if __name__ == '__main__':
    my_project = Project('../users.json')
    my_project.entrance('Антон', 12)
    my_project.add_user('Кирилл', 55, 1)
    print(*my_project.users, sep='\n')
