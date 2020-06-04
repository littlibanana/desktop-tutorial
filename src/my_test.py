import tkinter as tk

class Showing3Cats(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.widgets()
        self.title_words()

    def title_words(self):
        self.title = tk.Label(self, text='適配*3', bg='green')
        self.title.grid(row = 0, column = 0, columnspan=3, sticky = tk.NE + tk.SW)

    def widgets(self):
        self.image1 = tk.Label(self, bg='red')
        self.image2 = tk.Label(self, bg='blue')
        self.image3 = tk.Label(self, bg='yellow')
        self.info1 = tk.Label(self, text = 'name: \nage: \nothers: \nurl', anchor="w")
        self.info2 = tk.Label(self, text = 'name: \nage: \nothers: \nurl:', anchor="e")
        self.info3 = tk.Label(self, text = 'name: \nage: \nothers: \nurl', anchor="e")
        
        self.image1.grid(row = 1, column = 0, sticky = tk.NE + tk.SW)
        self.image2.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
        self.image3.grid(row = 1, column = 2, sticky = tk.NE + tk.SW)
        self.info1.grid(row = 2, column = 0, sticky = tk.W)
        self.info2.grid(row = 2, column = 1, sticky = tk.W)
        self.info3.grid(row = 2, column = 2, sticky = tk.W)

win = Showing3Cats()
win.master.title('cats')
win.master.geometry('800x600')
win.configure(background='white')
win.mainloop()