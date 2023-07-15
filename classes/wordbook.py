from paths import WORDBOOK_PATH
from random import choice


class Wordbook(object):
    def __init__(self):
        self._wordbook = []
        self._used_words = []
        self.load_words()

    def load_words(self) -> list:
        try:
            with open(WORDBOOK_PATH, mode='rt', encoding='utf-8') as words_file:
                self._wordbook = words_file.readline().split()
                if not self._wordbook:
                    raise FileExistsError('В файле словаря нет слов')
                return self._wordbook
        except FileNotFoundError:
            raise FileNotFoundError('Не найден файл со словарем игровых слов.')

    def give_all_wordbook(self) -> list:
        return self._wordbook

    def give_game_word(self) -> str:
        not_used_words = list(set(self._wordbook) - set(self._used_words))
        if not_used_words:
            game_word = choice(not_used_words)
        else:
            game_word = choice(self._wordbook)
            self._used_words = []
        return game_word

    def add_new_word(self, new_word: str) -> str:
        new_word = new_word.lower()
        if new_word in self._wordbook:
            return f'Слово "{new_word}" уже находится в словаре игровых слов.'
        try:
            with open(WORDBOOK_PATH, mode='at', encoding='utf-8') as words_file:
                words_file.write(f' {new_word}')
                self._wordbook.append(new_word)
                return f'Слово "{new_word}" добавлено в словарь игровых слов.'
        except FileNotFoundError:
            raise FileNotFoundError('Не найден файл со словарем игровых слов.')

    def del_word(self, some_word: str) -> str:
        some_word = some_word.lower()
        if some_word not in self._wordbook:
            return f'Слово "{some_word}" уже отсутствовало в словаре игровых слов.'
        try:
            with open(WORDBOOK_PATH, mode='wt', encoding='utf-8') as words_file:
                self._wordbook.remove(some_word)
                words_file.write(' '.join(self._wordbook))
                return f'Слово "{some_word}" удалено из словаря игровых слов.'
        except FileNotFoundError:
            raise FileNotFoundError('Не найден файл со словарем игровых слов.')
