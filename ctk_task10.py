import customtkinter as ctk

check_row = 5
TASKS = []


def do_task():
    global TASKS
    count = 0
    for task in TASKS:
        choice = task.get()
        count += choice
    lbl_count.configure(text=f'Сделано {count} задач!')
    lbl_count.grid(row=8, column=3, padx=10, pady=10)


def add_task():
    global check_row, TASKS
    my_text = entr_task.get()
    task = ctk.CTkCheckBox(master=root)
    task.configure(text=my_text, font=my_font, command=do_task)
    task.grid(row=check_row, column=3, padx=10, pady=10)
    TASKS.append(task)
    if len(TASKS) == 3:
        lbl_max.grid(row=9, column=3, padx=10, pady=10)
        btn_add.configure(state='disabled')
    check_row += 1


def remove_tasks():
    global check_row, TASKS
    btn_add.configure(state='normal')
    lbl_max.grid_forget()
    lbl_count.grid_forget()
    for task in TASKS:
        task.grid_forget()
    TASKS.clear()
    check_row = 5


def light():
    ctk.set_appearance_mode("light")
    rad_dark.deselect()


def dark():
    rad_light.deselect()
    ctk.set_appearance_mode("dark")


root = ctk.CTk()
root.title("Список дел")
root.geometry("1200x700")

rows, columns = 9, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Arial', size=20, weight='bold')
font_mini = ctk.CTkFont(family='Arial', size=12, weight='bold')
btn_font = ctk.CTkFont(family='Arial', size=15, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Список дел', font=my_font)

lbl_max = ctk.CTkLabel(master=root)
lbl_max.configure(text='Добавлено максимальное количество задач!', font=font_mini)

lbl_count= ctk.CTkLabel(master=root)
lbl_count.configure(text=f'Сделано 0 задач!')

rad_light = ctk.CTkRadioButton(master=root)
rad_light.configure(text='Светлый фон', font=my_font, command=light)

rad_dark = ctk.CTkRadioButton(master=root)
rad_dark.configure(text='Тёмный фон', font=my_font, command=dark)

entr_task = ctk.CTkEntry(master=root)
entr_task.configure(placeholder_text='Введите задачу', justify="center", state="normal", font=my_font)

lbl_tasks = ctk.CTkLabel(master=root)
lbl_tasks.configure(text='Задачи для выполнения:', font=my_font)

btn_add = ctk.CTkButton(master=root)
btn_add.configure(text="Добавить задачу", font=btn_font, command=add_task)

btn_remove = ctk.CTkButton(master=root)
btn_remove.configure(text="Удалить все задачи", font=btn_font, command=remove_tasks)
btn_remove.grid(row=4, column=2, padx=20, pady=20, sticky="ew")

rad_light.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
rad_dark.grid(row=0, column=4, padx=10, pady=10, sticky="ew")
lbl_start.grid(row=1, column=3, padx=10, pady=10)
entr_task.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")
btn_add.grid(row=3, column=2, padx=10, pady=10, sticky="ew")
btn_remove.grid(row=3, column=4, padx=10, pady=10, sticky="ew")
lbl_tasks.grid(row=4, column=3, padx=10, pady=10)

root.mainloop()
