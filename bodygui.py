from tkinter import *
from tkinter import ttk
import htmlgenerator
import bodycontentdb


class Window():

    def __init__(self, master):

        self.frame = ttk.Frame(master, relief = RAISED, padding=10)
        self.frame.grid(row = 0, column = 0)

        ttk.Label(self.frame, text = 'Enter new body text here:').grid(row = 0, column = 0)
        self.body = Text(self.frame, width = 56, height = 10)
        self.body.grid(row = 1, column = 0, columnspan = 2)

        self.submitbutton = ttk.Button(self.frame, text = 'Add New Entry', command = self.addNew)
        self.submitbutton.grid(row = 2, column = 1)

        ttk.Label(self.frame, text = 'Select from past entries:').grid(row = 3, column = 0)
        self.contents = Listbox(self.frame, width = 45)
        self.contents.grid(row = 4, column = 0, columnspan = 2)

        self.createbutton = ttk.Button(self.frame, text = 'Create Page', command = self.submit)
        self.createbutton.grid(row = 5, column = 1)

        # populate listbox with past entries

        entries = bodycontentdb.viewAll()
        for row in entries:
            self.contents.insert(END, row)

    def submit(self):
        # get selected line
        selectindex = self.contents.curselection()
        # get text
        selectrow = self.contents.get(selectindex)
        newtext = selectrow[1]
        htmlgenerator.createPage(newtext)
        bodycontentdb.updateUse(newtext)

        self.contents.delete(0, END)

        entries = bodycontentdb.viewAll()
        for row in entries:
            self.contents.insert(END, row)

    def addNew(self):
        newtext = self.body.get(1.0, END)
        bodycontentdb.newEntry(newtext)
        self.body.delete(1.0, END)

        self.contents.delete(0, END)

        entries = bodycontentdb.viewAll()
        for row in entries:
            self.contents.insert(END, row)



def main():

    root = Tk()
    root.wm_title("Webpage Text Entry")
    win = Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
