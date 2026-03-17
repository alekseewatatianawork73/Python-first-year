import customtkinter as ctk


def show_res():
    name = entry_name.get()
    age = entry_age.get()
    gender = cmb_gender.get()
    my_hobby = []
    for i in range(3):
        if hobby_checks[i].get():
            my_hobby.append(hobbies[i])
    lbl_res.configure(text=f'Ваша анкета: Имя - {name}, возраст - {age}, пол - {gender},{'\n'} увлечения - {my_hobby}')


def inf_clear():
    entry_name.delete(0, 'end')
    entry_age.delete(0, 'end')
    cmb_gender.set('Выберите пол')
    for ch in hobby_checks:
        ch.deselect()


# основная программа
root = ctk.CTk()
root.title("Анкета с фреймами")
root.geometry("1000x700")
root.configure(fg_color='lightyellow')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Courier', size=20, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Регистрация пользователя', font=my_font)

lbl_person = ctk.CTkLabel(master=root)
lbl_person.configure(text='Личные данные', font=my_font)

lbl_hobby = ctk.CTkLabel(master=root)
lbl_hobby.configure(text='Интересы и увлечения', font=my_font)

lbl_res = ctk.CTkLabel(master=root)
lbl_res.configure(text='Ваша анкета: ...', font=my_font)

# фрейм с личными данными пользователя
frm_person = ctk.CTkFrame(master=root, width=300, height=300)
frm_person.configure(fg_color='khaki', border_color='gold4', border_width=3, corner_radius=30)
frm_person.grid_propagate(False)

entry_name = ctk.CTkEntry(master=frm_person)
entry_name.configure(justify='center', font=my_font, placeholder_text='Введите имя', border_color='gold4')

entry_age = ctk.CTkEntry(master=frm_person)
entry_age.configure(justify='center', font=my_font, placeholder_text='Введите возраст', border_color='gold4')

cmb_gender = ctk.CTkComboBox(master=frm_person)
cmb_gender.configure(values=['Мужской', 'Женский'], font=my_font, justify='center', border_color='gold4', state='readonly')
cmb_gender.set('Выберите пол')

frm_person.columnconfigure(index=0, weight=1)
frm_person.rowconfigure(index=(0, 1, 2), weight=1)
entry_name.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
entry_age.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
cmb_gender.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# фрейм с интересами пользователя
frm_hobby = ctk.CTkFrame(master=root, width=300, height=300)
frm_hobby.configure(fg_color='khaki', border_color='gold4', border_width=3, corner_radius=30)
frm_hobby.grid_propagate(False)

frm_hobby.columnconfigure(index=0, weight=1)
frm_hobby.rowconfigure(index=(0, 1, 2), weight=1)

hobbies = ['Спорт', 'Творчество', 'Программирование']
hobby_checks = []
for i in range(3):
    ch = ctk.CTkCheckBox(master=frm_hobby)
    ch.configure(text=hobbies[i], font=my_font)
    ch.grid(row=i, column=0, padx=10, pady=10, sticky="ew")
    hobby_checks.append(ch)

# фрейм с кнопками
frm_btn = ctk.CTkFrame(master=root, width=300, height=150)
frm_btn.configure(fg_color='khaki', border_color='gold4', border_width=3, corner_radius=30)
frm_btn.grid_propagate(False)

btn_res = ctk.CTkButton(master=frm_btn)
btn_res.configure(text="Показать анкету", font=my_font, fg_color='goldenrod4', hover_color='goldenrod3', command=show_res)

btn_clear = ctk.CTkButton(master=frm_btn)
btn_clear.configure(text="Очистить данные", font=my_font, fg_color='goldenrod4', hover_color='goldenrod3', command=inf_clear)

frm_btn.columnconfigure(index=0, weight=1)
frm_btn.rowconfigure(index=(0, 1), weight=1)
btn_res.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
btn_clear.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# размещение элементов в основном окне
lbl_start.grid(row=0, column=3, padx=10, pady=10)
lbl_person.grid(row=1, column=2, padx=10, pady=10)
lbl_hobby.grid(row=1, column=4, padx=10, pady=10)
frm_person.grid(row=2, column=2, padx=10, pady=10)
frm_hobby.grid(row=2, column=4, padx=10, pady=10)
frm_btn.grid(row=2, column=3, padx=10, pady=10)
lbl_res.grid(row=3, column=2, columnspan=3, padx=10, pady=10)

root.mainloop()
