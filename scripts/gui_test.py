from tkinter import Tk, Label, Button, LEFT, RIGHT


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack(side=LEFT)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side=RIGHT)

    def greet(self):
        print("Greetings!")


def main():
    root = Tk()
    my_gui = MyFirstGUI(root)
    my_gui.greet()
    root.mainloop()


if __name__ == '__main__':
    main()
