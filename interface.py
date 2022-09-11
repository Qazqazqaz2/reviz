import tkinter as tk

import main

def str_to_sort_list():
    data = main.main()
    print(data)
    file = open('Отчёт.txt', 'w')
    for dt in data:
        file.write(dt[0]+'\n')
    file.close()



root = Tk()
root.geometry("500x500")

but = Button(text="Запуск программы")
lab = Label(width=100, fg='black', text='Нажмите на кнопку')


but.bind('<Button-1>', str_to_sort_list)

lab.pack()
but.pack()

root.mainloop()
#str_to_sort_list()
