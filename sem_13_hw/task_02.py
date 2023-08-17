import csv
import json
from os import mkdir, path
from datetime import datetime


class StudentException(Exception):
    pass


class StudentNameTitleException(StudentException):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'ФИО должны начинаться с большой буквы: {self.name}'


class StudentNameCharException(StudentException):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'ФИО должны содержать только буквы: {self.name}'


class MarkRangeException(StudentException):
    def __init__(self, mark: int, min_limit: int, max_limit: int):
        self.mark = mark
        self.min_limit = min_limit
        self.max_limit = max_limit

    def __str__(self):
        return f'Mark {self.mark} - should be in range {self.min_limit} - {self.max_limit}!'


class InvalidSubjectException(StudentException):
    def __init__(self, subject: str, subjects: set[str]):
        self.subject = subject
        self.subjects = subjects

    def __str__(self):
        return f'{self.subject.title()} - invalid subject! Should be one of the following:\n' \
                f'{self.subjects}'


class NameValidator:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not value.istitle():
            raise StudentNameTitleException(value)

        if not value.isalpha():
            raise StudentNameCharException(value)

        setattr(instance, self.name, value)


class Student:
    MARK_LIMITS = {
        'mark': (2, 5),
        'test': (0, 100)
    }

    first_name = NameValidator()
    last_name = NameValidator()
    patronymic = NameValidator()

    def __init__(self, first_name: str, last_name: str, patronymic: str):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic

        with open('subjects.csv', 'r', encoding='utf-8') as subjects_file:
            self.subjects = set(*csv.reader(subjects_file, dialect='excel'))

        self.data_path = f'students/{self.last_name.lower()}_{self.first_name.lower()}_{self.patronymic.lower()}.json'
        self.journal = self._load_data()

    def log_mark(self, subject: str, mark: int, comment: str = ''):
        self._add_data('mark', subject, mark, comment)

    def log_test(self, subject: str, mark: int, comment: str = ''):
        self._add_data('test', subject, mark, comment)

    def _add_data(self, category: str, subject: str, mark: int, comment: str = ''):
        if subject not in self.subjects:
            raise InvalidSubjectException(subject, self.subjects)
        if not isinstance(mark, int):
            raise TypeError(f'{mark} - {category} value should be integer number!')
        if not (self.MARK_LIMITS[category][0] <= mark <= self.MARK_LIMITS[category][1]):
            raise MarkRangeException(mark, self.MARK_LIMITS[category][0], self.MARK_LIMITS[category][1])
        log_dict = {
            'datetime': datetime.now().strftime("%d-%m-%Y %H:%M"),
            'mark': mark,
            'comment': comment
        }
        self.journal[subject][f'{category}s'].append(log_dict)
        self._dump_data()

    def _load_data(self):
        if path.exists(self.data_path):
            with open(self.data_path, 'r', encoding='utf-8') as journal_file:
                return json.load(journal_file)
        else:
            return {subject: {'marks': [], 'tests': []} for subject in self.subjects}

    def _dump_data(self):
        if not path.exists('students'):
            mkdir('students')
        with open(self.data_path, 'w', encoding='utf-8') as journal_file:
            json.dump(self.journal, journal_file, indent=2, ensure_ascii=False)

    def get_avg_subj_mark(self, subject: str):
        return round(self._get_avg_subj('marks', subject), 2)

    def get_avg_mark(self):
        return round(self._get_avg('marks'), 2)

    def get_avg_subj_test(self, subject: str):
        return round(self._get_avg_subj('tests', subject), 2)

    def get_avg_test(self):
        return round(self._get_avg('tests'), 2)

    def _get_avg_subj(self, category: str, subject: str):
        if subject not in self.subjects:
            raise InvalidSubjectException(subject, self.subjects)
        if len(self.journal[subject][category]) <= 0:
            return None
        return sum(mark['mark'] for mark in self.journal[subject][category]) / len(self.journal[subject][category])

    def _get_avg(self, category: str):
        marks = list(filter(lambda mark: mark, [self._get_avg_subj(category, subject) for subject in self.subjects]))
        if len(marks) > 0:
            return sum(marks) / len(marks)

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def __str__(self):
        return (f'Student: {self.get_full_name()}\n'
                f'Average mark: {self.get_avg_mark()}\n'
                f'Average test mark: {self.get_avg_test()}')


if __name__ == '__main__':
    # student_1 = Student('петр', 'Иванов', 'Олегович')
    # student_1 = Student('Петр', 'Иванов', 'Олег_ович')
    student_1 = Student('Иван', 'Петров', 'Васильевич')

    # student_1.log_mark('Maths', 7, 'classwork')
    # student_1.log_test('Геометрия', 89)
    student_1.log_mark('Maths', 2, 'classwork')

