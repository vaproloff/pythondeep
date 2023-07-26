import random

__all__ = ['generate_names_file']


def generate_name(name_len_min: int, name_len_max: int) -> str:
    vowels_list = 'аеиоуюяы'
    consonants_list = 'бвгджзклмнпрстфчхшщ'
    return ''.join(random.choice(vowels_list if random.choice([True, False]) else consonants_list)
                   for _ in range(random.randint(name_len_min, name_len_max)))


def generate_names_file(file_name='task_02_file.txt', limit=200) -> None:
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(limit + 1):
            file.write(generate_name(4, 7).capitalize() + '\n')


if __name__ == '__main__':
    generate_names_file()
