import random
from csv import DictReader
import tkinter as tk
from pathlib import Path

from question import Question
from scores import SUCCESS, FAILURE


root_path = Path(__file__).parents[1]


class Trainer:

    def __init__(self, window):
        self._window = window
        self._score = 0
        self._tired = -100

        with open(root_path / 'data/dictionary.csv', 'r') as storage:
            reader = DictReader(storage)
            self._pairs = [pair for pair in reader]

        self._select_question()
        # render
        self._window.render_score(self._score)

    def add_score(self, value):
        self._score += value
        if self._score <= self._tired:
            self._window.render_end()

    def handle_choice(self, choice_id):
        if self._question.is_resolved:
            return
        self._question.is_resolved = True
        is_success = (choice_id == self._question.answer_code)
        if is_success:
            self.add_score(SUCCESS)
        else:
            self.add_score(FAILURE)
        try:
            self._window.render_score(self._score)
            self._window.render_choice_result(choice_id, self._question.answer_code)
            self._window.render_next(True)
        except tk.TclError:
            pass

    def handle_next(self):
        self._select_question()

    def _select_question(self):
        random.shuffle(self._pairs)
        self._question = Question(self._pairs[0], [pair["translation"] for pair in self._pairs[1:5]])
        self._window.render_question(self._question)
        self._window.render_next(False)
