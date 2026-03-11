import customtkinter as ctk

checks = []  # список всех чекбоксов в окне
radios = []  # список всех радиокнопок в окне


# функция, срабатывающая при выборе чекбокса
def press_check():
    done_check = 0  # количество выбранных чекбоксов
    # перебираем все чекбоксы из списка checks
    for task in checks:
        # проверяем, что чекбокс выбран: task.get() = True (верно)
        if task.get():
            done_check += 1
    lbl_check.configure(text=f'Выбрано {done_check} чекбоксов')


# функция, срабатывающая при выборе радиокнопки
def press_radio():
    choice = radio_var.get()  # получаем текущее выбранное значение
    lbl_radio.configure(text=f'Выбрана радиокнопка {choice}')


# функция для кнопки "Добавить чекбокс"
def add_check():
    global checks
    my_text = entr.get()  # получаем текст из текстового поля entr
    # создаём чекбокс, задаём ему свойства и размещаем в окне
    task = ctk.CTkCheckBox(master=root)
    task.configure(text=f'Чекбокс {len(checks) + 1}: {my_text}', font=my_font, command=press_check)
    task.grid(row=len(checks) + 3, column=2, padx=10, pady=10)
    # добавляем чекбокс в список чекбоксов
    checks.append(task)


# функция для кнопки "Добавить радиокнопку"
def add_radio():
    global radios
    my_text = entr.get()  # получаем текст из текстового поля entr
    # создаём радиокнопку, задаём ей свойства и размещаем в окне
    task = ctk.CTkRadioButton(master=root, value=len(radios)+1)
    task.configure(text=f'Радиокнопка {len(radios) + 1}: {my_text}', font=my_font, command=press_radio, variable=radio_var)
    # variable - переменная для начального выбранного значения, value - значение текущей кнопки (будут по номеру в списке radios)
    task.grid(row=len(radios) + 3, column=4, padx=10, pady=10)
    # добавляем радиокнопку в список радиокнопок
    radios.append(task)


root = ctk.CTk()
root.title("Моё приложение")
root.geometry("1000x500")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Arial', size=20, weight='bold')

# создаём поле для ввода задач
entr = ctk.CTkEntry(master=root)
entr.configure(justify="center", state="normal", font=my_font, placeholder_text='Введите задачу')
# placeholder_text - серый текст подсказка внутри поля для ввода, пока оно пустое и не используется

# создаём кнопки для добавления чекбоксов и радиокнопок
btn_check = ctk.CTkButton(master=root)
btn_check.configure(text="Добавить чекбокс", font=my_font, command=add_check)

btn_radio = ctk.CTkButton(master=root)
btn_radio.configure(text="Добавить радиокнопку", font=my_font, command=add_radio)

# надписи для количества выбранных чекбоксов и радиокнопок, в начале 0
lbl_check = ctk.CTkLabel(master=root)
lbl_check.configure(text='Выбрано 0 чекбоксов')

lbl_radio = ctk.CTkLabel(master=root)
lbl_radio.configure(text='Выбрана радиокнопка ...')

# начальное выбранное значение среди радиокнопок: пусть будет 0
radio_var = ctk.IntVar(value=0)

# размещаем элементы в окне
lbl_check.grid(row=1, column=2, padx=10, pady=10)
lbl_radio.grid(row=1, column=4, padx=10, pady=10)
entr.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")
btn_check.grid(row=2, column=2, padx=10, pady=10, sticky="ew")
btn_radio.grid(row=2, column=4, padx=10, pady=10, sticky="ew")

root.mainloop()
