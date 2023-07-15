from paths import TEMPLATES_PATH
from abc import abstractmethod
import os


class Screen(object):
    @abstractmethod
    def show_gallows(self, mistakes: int):
        ...


class ConsoleScreen(Screen):
    def __init__(self):
        self.gallows_template = ''
        self.prisoner_template = []
        self.load_templates()

    def load_templates(self) -> None:
        try:
            with open(TEMPLATES_PATH, mode='rt', encoding='utf-8') as templates_file:
                self.prisoner_template = templates_file.readline().split()
                tmp = []
                for line in templates_file.readlines():
                    tmp.append(line)
                self.gallows_template = ''.join(tmp)
        except FileNotFoundError:
            raise FileNotFoundError(f'Не найден файл с изображением висилицы.')

    @staticmethod
    def clear_screen() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_gallows(self, making_mistakes: int) -> None:
        current_gallows = self.gallows_template
        max_mistakes = len(self.prisoner_template)
        for mistake in range(max_mistakes):
            replace_char = ' ' if mistake >= making_mistakes else self.prisoner_template[mistake]
            current_gallows = current_gallows.replace(str(mistake), replace_char)
        print(current_gallows)

    @staticmethod
    def show_word(game_word: str, good_symbols: list, bad_symbols: list) -> None:

        game_word_symbols = list(game_word)
        for index in range(len(game_word_symbols)):
            if game_word_symbols[index] in good_symbols:
                continue
            else:
                game_word_symbols[index] = '_'
        screen_word = 'Загадано слово [ ' + ' '.join(game_word_symbols) + ' ]'
        print(screen_word)
        if bad_symbols:
            print('В слове точно нет букв: ' + ', '.join(bad_symbols))

    @staticmethod
    def greetings() -> bool:
        user_input = input('Введите 1, если хотите начать новую игру, либо иной символ для выходы: ')
        if user_input == '1':
            return True
        else:
            exit(0)

    @staticmethod
    def show_get_new_symbol() -> str:
        user_input = input('Введите букву, которая есть в слове: ')
        return user_input

    @staticmethod
    def print_game_result(game_result: str) -> None:
        if game_result == 'win':
            print('Игра закончена: Вы выиграли!!!')
        elif game_result == 'fail':
            print('Игра закончена: Вы проиграли!!!')


class GameScreen(ConsoleScreen):
    def __init__(self):
        super().__init__()
