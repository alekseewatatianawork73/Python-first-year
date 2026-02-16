import customtkinter as ctk  # подключаем библиотеку customtkinter


# функция, срабатывающая при нажатии кнопки btn_result
def press():
    a = entry_input.get()  # получаем данные из поля ввода - сторона квадрата
    res = 0
    # проверяем, какое значение выбрано в выпадающем списке
    if cmb.get() == "Операция 1: периметр квадрата":
        res = int(a) * 4
    elif cmb.get() == "Операция 2: площадь квадрата":
        res = int(a)**2
    entry_output.configure(state="normal")  # чтобы записать ответ в поле, необходимо сделать его снова активным
    entry_output.delete(0, "end")  # удаляем предыдущее значение
    entry_output.insert(0, res)  # вставляем новое значение
    entry_output.configure(state="disabled")  # снова блокируем поле


# создаём главное окно
root = ctk.CTk()
root.title("Поиск площади и периметра квадрата")
root.geometry("1000x500")
root.configure(fg_color='darkseagreen1')

# создаём шрифт для нашего приложения
my_font = ctk.CTkFont(family='Times New Roman', size=20)

# текстовое поле для начального сообщения
lbl_start = ctk.CTkLabel(master=root)  # root - главное окно
lbl_start.configure(text="Выберите операцию из списка:", font=my_font)

# выпадающий список для выбора операции
operations = ["Операция 1: периметр квадрата", "Операция 2: площадь квадрата"]
cmb = ctk.CTkComboBox(master=root)
cmb.configure(justify="center", values=operations, state="readonly", font=my_font)
# justify - расположение текста (по центру), state - состояние списка (readonly - только для чтения)
cmb.set("Операция 1: периметр квадрата")  # значение по умолчанию при запуске приложения

# текстовые метки для обозначения окошек ввода и вывода
lbl_input, lbl_output = ctk.CTkLabel(master=root), ctk.CTkLabel(master=root)
lbl_input.configure(text="Сторона квадрата:", font=my_font)
lbl_output.configure(text="Результат:", font=my_font)
# поле для ввода
entry_input = ctk.CTkEntry(master=root)
entry_input.configure(justify="center", font=my_font)
# поле для вывода результата
entry_output = ctk.CTkEntry(master=root)
entry_output.configure(justify="center", state='disabled', font=my_font)
# кнопка получения результата
btn_result = ctk.CTkButton(master=root)
btn_result.configure(text="Получить результат", command=press, font=my_font, fg_color='darkgreen', hover_color='darkolivegreen')

# для расположения виджетов на экране используем сетку - grid
rows, columns = 7, 7
# пусть будет сетка 7 x 7, каждой строке и столбцу установим вес 1, чтобы сетка была равномерной
# индексы строк и столбцов начинаются с нуля
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

# теперь расположим в ней наши виджеты
# виджет можно расположить в одной ячейке, например, в ячейке (0, 2), тогда укажем row=0, column=2
# а можно - в нескольких, например, в ячейках (0, 1) и (0, 2), тогда укажем: row=0, column=1, columnspan=2
# то есть columnspan растягивает виджет на 2 столбца
lbl_start.grid(row=0, column=3, columnspan=2, padx=10, pady=10)
cmb.grid(row=1, column=3, columnspan=2, sticky="ew")
lbl_input.grid(row=2, column=1, padx=10, pady=10)
lbl_output.grid(row=2, column=5, padx=10, pady=10)
entry_input.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
entry_output.grid(row=3, column=5, padx=10, pady=10, sticky="nsew")
btn_result.grid(row=4, column=3, padx=10, pady=10, sticky="ew")

root.mainloop()
