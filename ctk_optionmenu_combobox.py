import customtkinter as ctk


# функция, которая выполняется при выборе элемента в списке Option Menu
def menu_func(elem):
    res = f'Вы выбрали {elem} из списка Option Menu'
    # вставляем строку res в текстовое поле entr_res
    entr_res.configure(state='normal')
    entr_res.delete(0, 'end')
    entr_res.insert(0, res)
    entr_res.configure(state='disabled')


# функция, которая выполняется при выборе операции в списке Combo Box
def cmb_func(oper):
    res = f'Вы выбрали {oper} из списка Combo Box'
    # вставляем строку res в текстовое поле entr_res
    entr_res.configure(state='normal')
    entr_res.delete(0, 'end')
    entr_res.insert(0, res)
    entr_res.configure(state='disabled')


# создание главного окна
root = ctk.CTk()
root.title("Выпадающие списки")
root.geometry("900x500")
root.configure(fg_color='mintcream')

# сетка для размещения элементов в окне: 7 строк и 7 столбцов
rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=20)  # шрифт приложения

# создание надписей (текстовых меток) в окне
lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text="Сравнение двух классов для выпадающих списков", font=my_font)

lbl_menu = ctk.CTkLabel(master=root)
lbl_menu.configure(text="Класс CTkOptionMenu:", font=my_font)

lbl_cmb = ctk.CTkLabel(master=root)
lbl_cmb.configure(text="Класс CTkComboBox:", font=my_font)

# создание выпадающего списка при помощи класса CTkOptionMenu
elements = ["Элемент 1", "Элемент 2", "Элемент 3"]
menu = ctk.CTkOptionMenu(master=root)
menu.configure(values=elements, font=my_font, command=menu_func, anchor='center')
menu.set("Option Menu")

# создание выпадающего списка при помощи класса CTkComboBox
operations = ["Операция 1", "Операция 2", "Операция 3"]
cmb = ctk.CTkComboBox(master=root)
cmb.configure(justify="center", values=operations, command=cmb_func, state="normal", font=my_font)
cmb.set('Combo Box')

# создание текстового поля для вывода
entr_res = ctk.CTkEntry(master=root)
entr_res.configure(justify='center', font=my_font, state='disabled')

# размещение элементов в окне
lbl_start.grid(row=0, column=3, padx=10, pady=10)
lbl_menu.grid(row=1, column=2, padx=10, pady=10)
lbl_cmb.grid(row=1, column=4, padx=10, pady=10)
menu.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
cmb.grid(row=2, column=4, padx=10, pady=10, sticky='ew')
entr_res.grid(row=3, column=3, padx=10, pady=10, sticky='nsew')

root.mainloop()  # цикл для отображения главного окна приложения
