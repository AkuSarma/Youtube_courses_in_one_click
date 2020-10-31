from tkinter import *
import webbrowser
from source import *
root = Tk()
root.title("All course in one click")
root.geometry("1530x700")
root.configure(background="black")


class links:
    def __init__(self):
        self.position = Frame(root, background="black")
        self.chemistry = Button(self.position, text="Chemistry", height=10,
                                width=30, font="family=Helvetica,size=80", bg="red", fg="white", command=self.chemistry)
        self.physics = Button(self.position, text="Physics", height=10,
                              width=30, font="family=Helvetica,size=80", bg="blue", fg="white", command=self.physics)
        self.maths = Button(self.position, text="Maths",
                            height=10, width=30, font="family=Helvetica,size=80", bg="green", fg="white", command=self.maths)
        self.back_button = Button(
            root, text="<<", bg="blue", fg="white", command=self.back)
        self.main_menu()

    def main_menu(self):
        self.position.pack(padx=30, pady=300)
        self.chemistry.pack(padx=15, side=LEFT)
        self.physics.pack(padx=15, side=LEFT)
        self.maths.pack(padx=15, side=LEFT)

    def start(self):
        self.contents = Frame(root, background="black")
        self.position.pack_forget()
        root.configure(background="green")
        self.back_button.pack(side=LEFT, anchor=NW, padx=10, pady=10)
        self.contents.pack(padx=40, pady=60)
        Label(self.contents, text="Contents", bg="black", fg="yellow").pack()

    def back(self):
        root.configure(background="black")
        self.contents.destroy()
        self.contents.pack_forget()
        self.back_button.pack_forget()
        self.main_menu()

    def chemistry(self):
        self.start()
        for i in range(len(Chemistry().chem_chaps)):
            Button(self.contents, text=Chemistry().chem_chaps[i], bg="black", fg="white",
                   command=lambda i=i: webbrowser.open(Chemistry().chem_links[i])).pack(pady=5)

    def physics(self):
        self.start()
        for i in range(len(Physics().physics_chaps)):
            Button(self.contents, text=Physics().physics_chaps[i], bg="black", fg="white",
                   command=lambda i=i: webbrowser.open(Physics().physics_links[i])).pack(pady=5)

    def maths(self):
        self.start()
        for i in range(len(Math().math_chaps)):
            Button(self.contents, text=Math().math_chaps[i], bg="black", fg="white",
                   command=lambda i=i: webbrowser.open(Math().math_links[i])).pack(pady=5)


links()
root.mainloop()
