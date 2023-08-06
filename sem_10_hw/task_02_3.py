PUZZLES = [
    {
        'puzzle': 'Чудо-ящик. В нём окно. В том окошечке — кино.',
        'answers': ['телевизор', 'телек']
    },
    {
        'puzzle': 'Резвый конь не ест овса, у него два колеса.',
        'answers': ['велосипед', 'мотоцикл']
    },
    {
        'puzzle': 'Весной в землю зарывали, а по осени копали.',
        'answers': ['картофель', 'картошка']
    }
]


class PuzzleGame:
    def __init__(self, puzzles: list[dict], trials_num: int):
        self.puzzles = puzzles
        self.current_puzzle = 0
        self.trials_num = trials_num
        self.stats = dict()

    def next_puzzle(self):
        puzzle = self.puzzles[self.current_puzzle]
        print(puzzle['puzzle'])
        for trial in range(self.trials_num):
            current_try = input(f'Осталось попыток: {self.trials_num - trial}. Ваш ответ: ').lower()
            if current_try in puzzle['answers']:
                print('Верно!')
                self.stats.update({puzzle['puzzle']: trial + 1})
                break
            else:
                print('Неверно!')
        else:
            print('К сожалению, попыток не осталось. Вы не угадали')
            self.stats.update({puzzle['puzzle']: 0})

    def show_stat(self) -> None:
        print('Статистика отгадывания:')
        output = '\n'.join((f'Загадка: {puzzle_text} '
                            f'{f"Угадана с {trial_count} попытки." if trial_count > 0 else "Не угадана."}'
                            for puzzle_text, trial_count in self.stats.items()))
        print('\n', output, sep='')

    def play(self):
        while self.current_puzzle < len(self.puzzles):
            self.next_puzzle()
            self.current_puzzle += 1
        self.show_stat()


if __name__ == '__main__':
    puzzle_game = PuzzleGame(PUZZLES, 2)
    puzzle_game.play()
