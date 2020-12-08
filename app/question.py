import random


class Question:
    def __init__(self, dictionary_line, choices):
        self.word = dictionary_line["word"]
        _answer_text = dictionary_line["translation"]
        self.choices = choices + [_answer_text]
        random.shuffle(self.choices)
        self.answer_code = self.choices.index(_answer_text) + 1
        self.is_resolved = False
