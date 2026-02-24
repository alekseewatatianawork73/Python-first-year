import customtkinter as ctk


def press():
    name, sur = entr_name.get(), entr_sur.get()
    age, form = ages.get(), forms.get()
    sub = entr_sub.get()
    lbl_res.configure(text=f'Моё имя - {sur} {name}. Мне {age} лет. Я учусь в {form} классе.{'\n'}Мой любимый школьный предмет - {sub}.')
    lbl_res.grid(row=4, column=1, columnspan=5, padx=10, pady=10, sticky='ew')


root = ctk.CTk()
root.title("Анкета ученика")
root.geometry("1000x500")
root.configure(fg_color='mintcream')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=20)

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text="Заполните анкету:", font=my_font)

lbl_name = ctk.CTkLabel(master=root)
lbl_name.configure(text="Введите имя:", font=my_font)

lbl_sur = ctk.CTkLabel(master=root)
lbl_sur.configure(text="Введите фамилию:", font=my_font)

lbl_age = ctk.CTkLabel(master=root)
lbl_age.configure(text="Выберите возраст:", font=my_font)

lbl_form = ctk.CTkLabel(master=root)
lbl_form.configure(text="Выберите класс:", font=my_font)

lbl_sub = ctk.CTkLabel(master=root)
lbl_sub.configure(text="Введите любимый предмет:", font=my_font)

lbl_res = ctk.CTkLabel(master=root)
lbl_res.configure(text="...", font=my_font)

age_list = ["11", "12", "13", "14", "15", "16", "17"]
ages = ctk.CTkComboBox(master=root)
ages.configure(justify="center", values=age_list, state="readonly", font=my_font)
ages.set('...')

form_list = ["5", "6", "7", "8", "9", "10", "11"]
forms = ctk.CTkComboBox(master=root)
forms.configure(justify="center", values=form_list, state="readonly", font=my_font)
forms.set('...')

entr_name = ctk.CTkEntry(master=root)
entr_name.configure(justify='center', font=my_font, state='normal')

entr_sur = ctk.CTkEntry(master=root)
entr_sur.configure(justify='center', font=my_font, state='normal')

entr_sub = ctk.CTkEntry(master=root)
entr_sub.configure(justify='center', font=my_font, state='normal')

btn_result = ctk.CTkButton(master=root)
btn_result.configure(text="Посмотреть результат", command=press, font=my_font, fg_color='mediumaquamarine', text_color='black')

lbl_start.grid(row=0, column=3, padx=10, pady=10)

lbl_name.grid(row=1, column=1, padx=10, pady=10)
lbl_sur.grid(row=1, column=2, padx=10, pady=10)
lbl_age.grid(row=1, column=3, padx=10, pady=10)
lbl_form.grid(row=1, column=4, padx=10, pady=10)
lbl_sub.grid(row=1, column=5, padx=10, pady=10)

entr_name.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
entr_sur.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
ages.grid(row=2, column=3, padx=10, pady=10)
forms.grid(row=2, column=4, padx=10, pady=10)
entr_sub.grid(row=2, column=5, padx=10, pady=10, sticky='ew')

btn_result.grid(row=3, column=3, padx=10, pady=10, sticky='ew')
lbl_res.grid(row=4, column=3, padx=10, pady=10, sticky='ew')

root.mainloop()
