# Приложение для преобразования строк к верхнему и нижнему регистру
import customtkinter as ctk


# функция для преобразования строки к верхнему регистру
def press1():
    s = entr.get()  # получаем строку s из поля для ввода entr
    s = s.upper()  # переводим в верхний регистр
    entr.delete(0, 'end')  # очищаем поле от старого значения
    entr.insert(0, s)  # вставляем новое значение s в поле


# функция для преобразования строки к нижнему регистру
def press2():
    s = entr.get()
    s = s.lower()
    entr.delete(0, 'end')
    entr.insert(0, s)


# создаём основное окно размером 1000x500
root = ctk.CTk()
root.geometry('1000x500')
root.title('Моё приложение')
# поменяем цвет фона
root.configure(fg_color='paleturquoise')

# сетка для размещения элементов в окне
r, c = 7, 7
for i in range(r):
    root.rowconfigure(i, weight=1)
for i in range(c):
    root.columnconfigure(i, weight=1)

# создаём шрифт для надписей в окне
my_font = font=ctk.CTkFont(family='Courier', size=20, weight='bold')

# создаём две кнопки для преобразования к верхним и нижним регистрам
btn_up = ctk.CTkButton(master=root)
btn_up.configure(text='Преобразовать в верхний регистр', command=press1, font=my_font, fg_color='royalblue')
btn_up.grid(row=3, column=3, padx=20, pady=20, sticky='ew')

btn_low = ctk.CTkButton(master=root)
btn_low.configure(text='Преобразовать в нижний регистр', command=press2, font=my_font, fg_color='royalblue')
btn_low.grid(row=4, column=3, padx=20, pady=20, sticky='ew')

# создаём тектовую надпись в окне
lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Работа со строками', font=my_font, fg_color='royalblue', text_color='white')
lbl.grid(row=0, column=3, padx=20, pady=20, sticky='ew')

# создаём поле для ввода текста, который нужно преобразовать
entr = ctk.CTkEntry(master=root)
entr.configure(justify='center', state='normal', font=my_font)
entr.grid(row=1, column=3, padx=20, pady=20, sticky='nsew')

root.mainloop()

# Доступные значения цветов для модуля customtkinter: https://letpy.com/handbook/tkinter-colors/
