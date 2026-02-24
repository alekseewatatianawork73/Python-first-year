import customtkinter as ctk


def menu_list(choice):
    if choice == 'Основные блюда':
        menu.configure(values=["Картофельное пюре с подливой", "Крем-суп сырный", "Паста Болоньезе",
                               "Суп куриный", "Салат Греческий"])
    elif choice == 'Десерты':
        menu.configure(values=["Тирамиссу", "Десерт Павлова", "Торт Наполеон",
                               "Медовик", "Мороженое"])
    else:
        menu.configure(values=["Кофе", "Чай чёрный", "Чай зелёный",
                               "Лимонад", "Сок"])


def press_add():
    food, count = menu.get(), entr_count.get()
    global order
    order += food + ' * ' + count + ', '
    lbl_res.configure(text=order)


def press_res():
    for widget in root.winfo_children():
        widget.grid_forget()
    lbl_finish.grid(row=3, column=3, padx=10, pady=10)


root = ctk.CTk()
root.title("Новый заказ!")
root.geometry("1000x500")
root.configure(fg_color='salmon')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=20)

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text="ОФОРМЛЕНИЕ ЗАКАЗА", font=my_font)

lbl_categ = ctk.CTkLabel(master=root)
lbl_categ.configure(text="Выберите категорию:", font=my_font)

lbl_pos = ctk.CTkLabel(master=root)
lbl_pos.configure(text="Выберите позицию в меню:", font=my_font)

lbl_count = ctk.CTkLabel(master=root)
lbl_count.configure(text="Введите количество:", font=my_font)

order = "Ваш заказ: "
lbl_res = ctk.CTkLabel(master=root)
lbl_res.configure(text=order, font=my_font)

lbl_finish = ctk.CTkLabel(master=root)
lbl_finish.configure(text="Ваш заказ принят!\nЗакройте меню и ожидайте :)", font=my_font)

categories = ["Основные блюда", "Десерты", "Напитки"]
cmb_categ = ctk.CTkComboBox(master=root)
cmb_categ.configure(justify="center", values=categories, state="readonly", font=my_font, command=menu_list)
cmb_categ.set('...')

positions = []
menu = ctk.CTkComboBox(master=root)
menu.configure(justify="center", values=positions, state="readonly", font=my_font)
menu.set('...')

entr_count = ctk.CTkEntry(master=root)
entr_count.configure(justify='center', font=my_font, state='normal')

btn_add = ctk.CTkButton(master=root)
btn_add.configure(text="Добавить в заказ", command=press_add, font=my_font, fg_color='red3', hover_color='red4')

btn_result = ctk.CTkButton(master=root)
btn_result.configure(text="Готово!", command=press_res, font=my_font, fg_color='red3', hover_color='red4')

lbl_start.grid(row=0, column=3, padx=10, pady=10)

lbl_categ.grid(row=1, column=2, padx=10, pady=10)
lbl_pos.grid(row=1, column=3, padx=10, pady=10)
lbl_count.grid(row=1, column=4, padx=10, pady=10)

cmb_categ.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
menu.grid(row=2, column=3, padx=10, pady=10, sticky='ew')
entr_count.grid(row=2, column=4, padx=10, pady=10, sticky='ns')

btn_add.grid(row=3, column=3, padx=10, pady=10, sticky='ew')
lbl_res.grid(row=4, column=2, columnspan=3, padx=10, pady=10)
btn_result.grid(row=5, column=3, padx=10, pady=10, sticky='ew')

root.mainloop()
