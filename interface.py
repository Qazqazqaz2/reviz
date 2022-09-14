from tkinter import *
from tkinter import filedialog as tkFileDialog

import main

filename = ''
def str_to_sort_list(event):
    print(filename)
    data = main.main(filename)
    file = open('Отчёт.txt', 'w')
    for dt in data:
        file.write(str(dt[0])+'\n')
    file.close()

def browsefunc():
    global filename
    filename = tkFileDialog.askopenfilename(filetypes=(("xlsx files","*.xlsx"),("All files","*.*")))
    ent1.insert(END, filename) # add this


root = Tk()
root.geometry("500x500")

ent1=Entry(root,font=40)
ent1.pack()

but = Button(text="Запуск программы")
lab = Label(width=100, fg='black', text='Нажмите на кнопку')


but.bind('<Button-1>', str_to_sort_list)

b1=Button(root,text="DEM",font=40,command=browsefunc)
b1.pack()

lab.pack()
but.pack()

root.mainloop()
#str_to_sort_list()
