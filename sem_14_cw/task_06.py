# Задание No6
# 📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# 📌 Напишите 3-7 тестов pytest для данного проекта.
# 📌 Используйте фикстуры.

from user_management.project import User, Project

import pytest


@pytest.fixture
def create_users():
    return {User('Кирилл', 55, 1),
            User('Иван', 13, 2),
            User('Антон', 12, 2),
            User('Константин', 23, 4)}


def test_load(create_users):
    project = Project('users.json')
    assert project.users == create_users


@pytest.fixture
def temp_project(tmp_path):
    return Project(str(tmp_path / 'users.json'))


@pytest.fixture
def add_users(temp_project):
    temp_project.admin_user = User('Валера', 1, 5)
    temp_project.add_user('Кирилл', 55, 1)
    temp_project.add_user('Иван', 13, 2)
    temp_project.add_user('Антон', 12, 2)
    temp_project.add_user('Константин', 23, 4)
    return temp_project


def test_adding_users(add_users, create_users):
    assert add_users.users == create_users


def test_entrance(add_users):
    add_users.entrance('Константин', 23)
    assert add_users.admin_user == User('Константин', 23, 4)


def test_print():
    name = 'Валера'
    user_id = 1
    user_level = 5
    assert str(User(name, user_id, user_level)) == f'name: {name}, id: {user_id}, level: {user_level}'


if __name__ == '__main__':
    pytest.main(['-vv'])
