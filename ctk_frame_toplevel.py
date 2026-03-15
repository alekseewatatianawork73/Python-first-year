# приложение для добавления виджетов внутри фрейма
# темы занятия: : создание фрейма CTkFrame, создание дополнительного окна CTkTopLevel, использование глобальных переменных, повторение пройденного
import customtkinter as ctk

# глобальные переменные
window = None  # дополнительное окно для добавления виджетов
widgets = None  # выпадающий список с виджетами, которые можно добавить
row_number = 0  # строка во фрейме, на которой отобразится новый виджет (начинаем с нулевой)

'''
1. Мы сделали дополнительное окно window глобальной переменной для того, чтобы при повторном нажатии кнопки "Добавить виджет" 
закрывать старое окно перед открытием нового. Пока window = None, его не существует, это пустая переменная, 
но если window не None, то окно уже было создано - такая проверка будет выполняться в начале функции add_window.
Без глобальной переменной мы не смогли бы получить доступ к созданному ранее окну внутри функции add_window().
2. Мы сделали выпадающий список widgets глобальной переменной, чтобы получить доступ к выбранному значению в функции add_widget().
Список widgets создаётся в одной функции (add_window), а используется в другой (add_widget). 
Без глобальной переменной функция add_widget не увидит этот список.
3. Мы сделали переменную row_number глобальной, чтобы запоминать, на какой строке размещать следующий виджет, 
и увеличивать номер строки после каждого добавления на 1 (то есть переходить на следующую строку).
Если не менять номер строки, то все виджеты будут накладываться друг на друга.
'''


# функция для кнопки "Добавить" - добавляет выбранный в списке widgets виджет на фрейм в главном окне
def add_widget():
    global widgets, row_number
    widget = widgets.get()  # получаем выбранный элемент в списке widgets

    # проверяем, какой виджет был выбран, и создаём его на фрейме frm
    if widget == 'Надпись':
        lbl_temp = ctk.CTkLabel(master=frm)
        lbl_temp.configure(text='Надпись на фрейме', font=my_font)
        lbl_temp.grid(row=row_number, column=0, padx=10, pady=10)
    elif widget == 'Кнопка':
        btn_temp = ctk.CTkButton(master=frm)
        btn_temp.configure(text="Кнопка на фрейме", font=my_font, fg_color='darkblue')
        btn_temp.grid(row=row_number, column=0, padx=10, pady=10, sticky="ew")
    elif widget == 'Текстовое поле':
        entry_temp = ctk.CTkEntry(master=frm)
        entry_temp.configure(justify="center", font=my_font)
        entry_temp.grid(row=row_number, column=0, padx=10, pady=10, sticky="ew")

    row_number += 1  # строка row_number уже занята => переходим на следующую строку


# функция для кнопки "Добавить виджет" - создаёт дополнительное окно для выбора добавляемого виджета
def add_window():
    global widgets, window
    # если окно уже было открыто, то удаляем его
    if window:
        window.destroy()

    # создаём новое дополнительное окно при помощи класса CTkToplevel
    window = ctk.CTkToplevel(master=root)
    window.title('Добавить виджет')  # заголовок окна
    window.geometry('700x500')  # размеры окна в пикселях
    window.resizable(False, False)  # запрет на изменение размеров окна по ширине и по высоте (если разрешаете - True)
    window.configure(fg_color='lightcyan')  # цвет фона окна
    window.attributes('-topmost', True)  # располагаем это окно над главным окном root (необязательно)

    # создаём сетку для размещения элементов (7 строк и 7 столбцов)
    r, c = 7, 7
    for i in range(r):
        window.rowconfigure(index=i, weight=1)
    for i in range(c):
        window.columnconfigure(index=i, weight=1)

    # создаём виджеты в окне winndow и размещаем их
    lbl_what = ctk.CTkLabel(master=window)
    lbl_what.configure(text='Какой виджет желаете добавить?', font=my_font)

    widgets = ctk.CTkComboBox(master=window)
    widgets.configure(values=['Надпись', 'Кнопка', 'Текстовое поле'], font=my_font, justify='center', dropdown_font=my_font)
    widgets.set('Выберите виджет из списка')

    btn_add = ctk.CTkButton(master=window)
    btn_add.configure(text="Добавить", font=my_font, fg_color='darkblue', command=add_widget)

    lbl_what.grid(row=0, column=3, padx=10, pady=10)
    widgets.grid(row=1, column=3, padx=10, pady=10, sticky="ew")
    btn_add.grid(row=2, column=3, padx=10, pady=10, sticky="ew")


# основная программа
root = ctk.CTk()
root.title("Добавление виджетов")
root.geometry("1000x700")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Courier', size=20, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Добавление виджетов внутри фрейма', font=my_font)

# создаём фрейм при помощи класса CTkFrame, при создании нужно указать размеры фрейма (в пикселях)
frm = ctk.CTkFrame(master=root, width=300, height=300)
frm.configure(fg_color='lightblue', border_color='darkblue', border_width=3, corner_radius=0)
# fg_color - цвет фона, border_color - цвет границы, border_width - ширина границы в пикселях
# corner_radius - радиус скругления углов (от 0 до 180), 0 - квадратные углы, 10 - немного скругленные,
# 50 - сильно скругленные, 180 - получите круглый фрейм
frm.grid_propagate(False)  # запрещаем фрейму изменять свои размеры (необязательно)

btn = ctk.CTkButton(master=root)
btn.configure(text="Добавить виджет", font=my_font, fg_color='darkblue', command=add_window)

lbl_start.grid(row=0, column=3, padx=10, pady=10)
frm.grid(row=1, column=3, padx=10, pady=10)
btn.grid(row=2, column=3, padx=10, pady=10, sticky="ew")

root.mainloop()
