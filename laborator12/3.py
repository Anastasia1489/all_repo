from tkinter import *

class IceCreamStand:
    def init(self):
        self.names = ['Магнат', 'Коровка', 'Вологодский пломбир', 'Карамелька', 'Шоколадная крошка', 'Макфлури']
        self.types = ['Эскимо', 'Стаканчик', 'Брикет', 'Просто мороженое', 'Пломбир', 'Мороженое']
    def get_names(self):
        return self.names
    def get_types(self):
        return self.types

class IceCreamStandGUI:
    def init(self, master):
        self.master = master
        master.title('IceCream')
        self.ice_cream_stand = IceCreamStand()
        self.names_label = Label(master, text='Название', font='Calibri 12 italic bold')
        self.names_listbox = Listbox(master, font='Calibri 12', height=len(self.ice_cream_stand.get_names()))
        for name in self.ice_cream_stand.get_names():
            self.names_listbox.insert(END, name)
        self.types_label = Label(master, text='Вид', font='Calibri 12 italic bold')
        self.types_listbox = Listbox(master, font='Calibri 12', height=len(self.ice_cream_stand.get_types()))
        for type in self.ice_cream_stand.get_types():
            self.types_listbox.insert(END, type)
        self.names_label.grid(row=0, column=0)
        self.names_listbox.grid(row=1, column=0)
        self.types_label.grid(row=0, column=1)
        self.types_listbox.grid(row=1, column=1)


root = Tk()
a = IceCreamStandGUI(root)
root.mainloop()
