import customtkinter as ctk

RASP = {"Понедельник": "Алгебра, Литература, История",
        "Вторник": "Русский язык, Физкультура, География",
        "Среда": "Геометрия, Биология, Алгебра",
        "Четверг": "Русский язык, Информатика, Английский язык",
        "Пятница": "Алгебра, Литература, Физкультура",
        "Суббота": "Выходной!",
        "Воскресенье": "Выходной!"}


def choice(day):
    rasp = RASP[day]
    entr_res.configure(state='normal')
    entr_res.delete(0, 'end')
    entr_res.insert(0, rasp)
    entr_res.configure(state='disabled')


root = ctk.CTk()
root.title("Моё расписание")
root.geometry("1000x500")
root.configure(fg_color='mintcream')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=20)

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text="Расписание уроков на неделю", font=my_font)

lbl_day = ctk.CTkLabel(master=root)
lbl_day.configure(text="Выберите день недели:", font=my_font)

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
week_menu = ctk.CTkOptionMenu(master=root)
week_menu.configure(values=days, font=my_font, command=choice, anchor='center', text_color='black', fg_color='mediumaquamarine', button_color='mediumseagreen')
week_menu.set("Дни недели")

entr_res = ctk.CTkEntry(master=root)
entr_res.configure(justify='center', font=my_font, state='disabled')

lbl_start.grid(row=0, column=3, padx=10, pady=10)
lbl_day.grid(row=1, column=3, padx=10, pady=10)
week_menu.grid(row=2, column=3, padx=10, pady=10, sticky='ew')
entr_res.grid(row=3, column=2, columnspan=3, padx=10, pady=10, sticky='nsew')

root.mainloop()
