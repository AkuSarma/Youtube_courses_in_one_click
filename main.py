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

    def mainMenu(self):
        
        labelMain = Label(self.mainFrame, text="Online courses", width=20).pack(pady=10)
        classXI = Button(self.mainFrame, text="class XI", width=20, command=self.classXI).pack(pady=10)
        classXII = Button(self.mainFrame, text="class XII", width=20, command=self.classXII).pack(pady=10)

        self.mainFrame.pack(pady=200)
    
    def classXI(self):
        self.mainFrame.destroy()
        self.mainFrame.pack_forget()

        chemistry = Button(self.classXIFrame, text="chemistry", width=20, command=lambda: self.chapters('classXI', 'chemistry')).pack(pady=10)
        physics = Button(self.classXIFrame, text="Physics", width=20, command=lambda: self.chapters('classXI', 'physics')).pack(pady=10)
        maths = Button(self.classXIFrame, text="Maths", width=20, command=lambda: self.chapters('classXI', 'maths')).pack(pady=10)

        self.classXIFrame.pack(pady=200)

    def classXII(self):
        self.mainFrame.destroy()
        self.mainFrame.pack_forget()

        chemistry = Button(self.classXIIFrame, text="chemistry", width=20, command=lambda: self.chapters('classXII', 'chemistry')).pack(pady=10)
        physics = Button(self.classXIIFrame, text="Physics", width=20, command=lambda: self.chapters('classXII', 'physics')).pack(pady=10)
        maths = Button(self.classXIIFrame, text="Maths", width=20, command=lambda: self.chapters('classXII', 'maths')).pack(pady=10)

        self.classXIIFrame.pack(pady=200)

    def chapters(self, classno, subject):
        if classno=="classXII":
            self.classXIIFrame.destroy()
            self.classXIIFrame.pack_forget()
        else:
            self.classXIFrame.destroy()
            self.classXIFrame.pack_forget()
        global data
        
        subjects = []
        links = []
        
        for key in data[classno][subject]:
            subjects.append(key)

        for i in subjects:
            links.append(data[classno][subject][i])

        for index, subject in enumerate(subjects):
            subject = Button(self.chaptersFrame, text=subject, width=50, command=lambda: webbrowser.open(links[index]))
            
            subject.pack(pady=3)

        self.chaptersFrame.pack(pady=50)


if __name__ == '__main__':
    run = Main()
    run.mainMenu()

    root.mainloop()