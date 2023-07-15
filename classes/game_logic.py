from classes.screen import GameScreen
from classes.wordbook import Wordbook


class GameLogic(object):
    def __init__(self):
        self.alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.wordbook = Wordbook()
        self.screen = GameScreen()
        self.used_symbols = []
        self.good_symbols = []
        self.bad_symbols = []
        self.game_word = ''

    def validate_user_input(self, user_input) -> bool:
        return True if len(user_input) == 1 and user_input in self.alphabet else False

    def new_game(self):
        self.used_symbols = []
        self.good_symbols = []
        self.bad_symbols = []
        self.game_word = self.wordbook.give_game_word()
        self.screen.greetings()
        mistakes = 0
        while True:
            while True:
                self.screen.clear_screen()
                self.screen.show_gallows(mistakes)
                self.screen.show_word(self.game_word, self.good_symbols, self.bad_symbols)
                new_symbol = self.screen.show_get_new_symbol().lower()
                if not self.validate_user_input(new_symbol):
                    continue
                if new_symbol in self.game_word:
                    self.good_symbols.append(new_symbol)
                elif new_symbol in self.bad_symbols:
                    continue
                else:
                    self.bad_symbols.append(new_symbol)
                    mistakes += 1
                break
            if mistakes == len(self.screen.prisoner_template):
                self.screen.print_game_result(game_result='fail')
                break
            if set(self.game_word) == set(self.good_symbols):
                self.screen.print_game_result(game_result='win')
                break
