import tkinter as tk
from tkinter import messagebox

from scores import SUCCESS, FAILURE


class Window:
    def __init__(self, master):
        self._handler = None
        self._master = master
        self.after = master.after
        _title = "word trainer".upper()
        master.title(_title)

        _title_frame = tk.Frame(master, width=500)
        _title_frame.pack(fill=tk.X)

        # header
        _header_frame = tk.Frame(master)
        _header_frame.pack(fill=tk.X)

        # score frame
        _score_frame = tk.Frame(_header_frame, height=100, width=100)
        _score_frame.pack(fill=tk.Y, side=tk.LEFT)
        self._score = tk.Label(_score_frame, text="LABEL", width=10)
        self._score.pack()

        # legend frame
        _legend_frame = tk.Frame(_header_frame, width=100, height=100)
        _legend_frame.pack(fill=tk.Y, side=tk.RIGHT)
        _legend_title = tk.Label(_legend_frame, text='Legend: ')
        _legend_title.pack(side=tk.LEFT)
        _legend_text = tk.Label(_legend_frame, text=f"OK: {SUCCESS}\nFAIL: {FAILURE}", justify=tk.LEFT)
        _legend_text.pack()

        # content_frame
        _content_frame = tk.Frame(master)
        _content_frame.pack(fill=tk.X)

        _word_frame = tk.Frame(_content_frame)
        _word_frame.pack()

        _word_label = tk.LabelFrame(_word_frame, text='Word:')
        _word_label.pack(side=tk.LEFT)
        self._word = tk.Label(_word_label, font='Arial 30', padx=10)
        self._word.pack(side=tk.LEFT)

        self._next_btn = tk.Button(_word_frame, text='NEXT', command=lambda: self._handler.handle_next())
        # self._next_btn.pack(side=tk.BOTTOM, padx=10)

        self._choices_frame = tk.Frame(_content_frame, pady=20)
        self._choices_frame.pack()

    def set_handler(self, value):
        self._handler = value

    def render_score(self, score):
        background = 'green' if score >= 0 else 'red'
        self._score.configure(
            text=f"Score: \n {score}",
            bg=background,
            fg='white'
        )

    def _get_choice_handler(self, i):
        def handle_choice():
            self._handler.handle_choice(i)
        return handle_choice

    def render_question(self, query):
        # render new word as well
        self._word.configure(text=query.word)
        # clear
        for widget in self._choices_frame.winfo_children():
            widget.destroy()
        # render new
        for i in range(len(query.choices)):
            _choice_id = i + 1
            _choice_btn = tk.Button(self._choices_frame, text=query.choices[i],
                                    command=self._get_choice_handler(_choice_id))
            _choice_btn.pack(side=tk.LEFT)

    def render_choice_result(self, choice_id, correct_id):
        # disable choices
        buttons = self._choices_frame.winfo_children()
        for _choice_btn in buttons:
            _choice_btn.configure(state=tk.DISABLED)
        # render result
        if choice_id == correct_id:
            buttons[choice_id -1].configure(bg='green')
        else:
            buttons[choice_id - 1].configure(bg='red')
            buttons[correct_id -1].configure(bg='green')

    def render_next(self, is_show):
        if is_show:
            self._next_btn.pack(side=tk.BOTTOM, padx=10)
        else:
            self._next_btn.pack_forget()

    def render_end(self):
        # "You looks tired, try later"
        messagebox.showerror('Tired Error', 'You looks tired, try later...')
        self._master.destroy()
