#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox

from trainer import Trainer
from window import Window


def main():
    root = tk.Tk()
    window = Window(root)
    trainer = Trainer(window)
    window.set_handler(trainer)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == '__main__':
    main()
