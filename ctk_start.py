
# импортируем библиотеку
import customtkinter as ctk


# функция-обработчик события нажатия кнопки btn
def press_btn():
    print('Кнопка нажата.')


# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("light")  # тема фона
ctk.set_default_color_theme("blue")  # тема виджетов

# создаём основное окно
root = ctk.CTk()
# устанавливаем название окна
root.title("Моё приложение")
# задаём размеры окна
root.geometry("1000x500")

# создадим в нашем окне 7 строк и 7 столбцов для размещения элементов
rows, columns = 7, 7
# будет сетка 7 x 7, каждой строке и столбцу установим вес 1, чтобы сетка была равномерной
# индексы строк и столбцов начинаются с нуля
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

# создание текстового поля
lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Простое приложение с кнопкой', font=ctk.CTkFont(family='Arial', size=25, weight='bold', slant='italic'))
lbl.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

#создание поля для ввода
entr = ctk.CTkEntry(master=root)
entr.configure(justify="center", state="normal")
entr.grid(row=2, column=2, columnspan=3, padx=20, pady=20, sticky="nsew")

# создание кнопки в главном окне root
btn = ctk.CTkButton(master=root)
# задание свойств кнопки
btn.configure(text="Получить результат", font=ctk.CTkFont(family='Arial', size=15), command=press_btn)
# размещение кнопки в 3 строке и в 3 столбце
btn.grid(row=3, column=3, padx=20, pady=20, sticky="ew")

# запускаем бесконечный цикл для отображения окна
root.mainloop()
