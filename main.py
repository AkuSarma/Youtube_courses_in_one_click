from tkinter import *
import json
import webbrowser

root = Tk()
root.geometry("1200x700")
root.title("All videos in one click")

data = {}
with open("source.json", "r") as f:
    data = json.load(f)


class Main():
    def __init__(self) -> None:
        self.mainFrame = Frame(root)
        self.classXIFrame = Frame(root)
        self.classXIIFrame = Frame(root)
        self.chaptersFrame = Frame(root)
        self.backButton = Button(root, text="back", command=self.back)
        self.currentScreen = ""

    def mainMenu(self):
        self.currentScreen = "mainMenu"
        
        labelMain = Label(self.mainFrame, text="Online courses", width=20).grid(row=0, column=0, columnspan=3, pady=40)
        classXI = Button(self.mainFrame, text="class XI", width=20, command=self.classXI).grid(row=1, column=0, padx=20)
        classXII = Button(self.mainFrame, text="class XII", width=20, command=self.classXII).grid(row=1, column=1, padx=20)

        self.mainFrame.pack(pady=200)
    
    def classXI(self):
        if self.currentScreen == "mainMenu":
            self.mainFrame.pack_forget()

            self.backButton.pack(anchor=NW)

            chemistry = Button(self.classXIFrame, text="chemistry", width=20, command=lambda: self.chapters('classXI', 'chemistry')).pack(pady=10)
            physics = Button(self.classXIFrame, text="Physics", width=20, command=lambda: self.chapters('classXI', 'physics')).pack(pady=10)
            maths = Button(self.classXIFrame, text="Maths", width=20, command=lambda: self.chapters('classXI', 'maths')).pack(pady=10)

        self.currentScreen = "classXI"

        self.classXIFrame.pack(pady=200)

    def classXII(self):
        if self.currentScreen == "mainMenu":
            self.mainFrame.pack_forget()

            self.backButton.pack(anchor=NW)

            chemistry = Button(self.classXIIFrame, text="chemistry", width=20, command=lambda: self.chapters('classXII', 'chemistry')).pack(pady=10)
            physics = Button(self.classXIIFrame, text="Physics", width=20, command=lambda: self.chapters('classXII', 'physics')).pack(pady=10)
            maths = Button(self.classXIIFrame, text="Maths", width=20, command=lambda: self.chapters('classXII', 'maths')).pack(pady=10)

        self.currentScreen = "classXII"

        self.classXIIFrame.pack(pady=200)

    def chapters(self, classno, subject):
        if classno=="classXII":
            self.classXIIFrame.pack_forget()
            self.currentScreen = "chaptersClassXII"
        else:
            self.classXIFrame.pack_forget()
            self.currentScreen = "chaptersClassXI"
        global data
        
        subjects = []
        links = []
        
        for key in data[classno][subject]:
            subjects.append(key)

        for i in subjects:
            links.append(data[classno][subject][i])

        self.backButton.pack(anchor=NW)

        for index, subject in enumerate(subjects):
            subject = Button(self.chaptersFrame, text=subject, width=50, command=lambda: webbrowser.open(links[index]))
            
            subject.pack(pady=3)

        self.chaptersFrame.pack(pady=50)

    def back(self):
        if self.currentScreen == "classXII":
            self.classXIIFrame.pack_forget()
            self.backButton.pack_forget()
            self.mainMenu()

        elif self.currentScreen == "classXI":
            self.classXIFrame.pack_forget()
            self.backButton.pack_forget()
            self.mainMenu()

        elif self.currentScreen == "chaptersClassXII":
            self.chaptersFrame.pack_forget()
            self.classXII()

        else:
            self.chaptersFrame.pack_forget()
            self.classXI()


if __name__ == '__main__':
    run = Main()
    run.mainMenu()

    root.mainloop()