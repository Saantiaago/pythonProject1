

from pyodbc import Row

from mainApp import *
from queries import *


def menu():
    window = Tk()
    window.title('Auth')
    window.geometry('450x250')
    window.resizable(False, False)
    window['background'] = 'white'

    font_header = ('Times New Roman', 15, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}


    getMenuList()

    window.mainloop()