import customtkinter as ctk


# функция для кнопки "Закрыть окно"
def no_window():
    window.destroy()
    # если окно закрыто, то его нельзя изменить => блокируем все виджеты
    btn_ic.configure(state='disabled')
    btn_deic.configure(state='disabled')
    btn_dest.configure(state='disabled')
    rad_white.configure(state='disabled')
    rad_yellow.configure(state='disabled')
    rad_red.configure(state='disabled')


# функция для радиокнопок - срабатывает при выборе одной из них
def fon_color():
    color = rad_var.get()  # получаем значение выбранной радиокнопки - white, yellow или red
    window.configure(fg_color=color)  # меняем цвет фона окна window


# основная программа
# главное окно root
root = ctk.CTk()
root.title("Методы дополнительного окна")
root.geometry("1200x700")

# сетка для главного окна: 7 строк и 7 столбцов
rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=20, weight='bold')

# дополнительное окно window
window = ctk.CTkToplevel(master=root)
window.title('Моё окно')
window.geometry('700x500')
window.attributes('-topmost', True)

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Работа с дополнительным окном', font=my_font)

# левый фрейм - действия над окном
frm_left = ctk.CTkFrame(master=root, width=400, height=500)
frm_left.configure(border_width=3, corner_radius=30)
frm_left.grid_propagate(False)

# элементы левого фрейма
lbl_btn = ctk.CTkLabel(master=frm_left)
lbl_btn.configure(text='Выберите действие: ', font=my_font)

btn_ic = ctk.CTkButton(master=frm_left)
btn_ic.configure(text="Свернуть окно", font=my_font, fg_color='darkblue', command=window.iconify)

btn_deic = ctk.CTkButton(master=frm_left)
btn_deic.configure(text="Развернуть окно", font=my_font, fg_color='darkblue', command=window.deiconify)

btn_dest = ctk.CTkButton(master=frm_left)
btn_dest.configure(text="Закрыть окно", font=my_font, fg_color='darkblue', command=no_window)

# сетка для левого фрейма
frm_left.columnconfigure(index=0, weight=1)  # один столбец с номером 0
frm_left.rowconfigure(index=(0, 1, 2, 3), weight=1)  # 4 строки с номерами 0, 1, 2, 3
# размещение элементов в левом фрейме
lbl_btn.grid(row=0, column=0, padx=10, pady=10)
btn_ic.grid(row=1, column=0, padx=10, pady=10)
btn_deic.grid(row=2, column=0, padx=10, pady=10)
btn_dest.grid(row=3, column=0, padx=10, pady=10)

# правый фрейм - для изменения цвета фона окна window
frm_right = ctk.CTkFrame(master=root, width=400, height=500)
frm_right.configure(border_width=3, corner_radius=30)
frm_right.grid_propagate(False)

# элементы правого фрейма
lbl_choice = ctk.CTkLabel(master=frm_right)
lbl_choice.configure(text='Выберите цвет фона: ', font=my_font)

rad_var = ctk.StringVar(value='white')  # группа радиокнопок (значение при запуске - white)
rad_white = ctk.CTkRadioButton(master=frm_right, value='white')
rad_white.configure(text='Белый', font=my_font, command=fon_color, variable=rad_var)
rad_yellow = ctk.CTkRadioButton(master=frm_right, value='yellow')
rad_yellow.configure(text='Желтый', font=my_font, command=fon_color, variable=rad_var)
rad_red = ctk.CTkRadioButton(master=frm_right, value='red')
rad_red.configure(text='Красный', font=my_font, command=fon_color, variable=rad_var)

# сетка для правого фрейма
frm_right.columnconfigure(index=0, weight=1)  # один столбец с номером 0
frm_right.rowconfigure(index=(0, 1, 2, 3), weight=1)  # 4 строки с номерами 0, 1, 2, 3
# размещение элементов в правом фрейме
lbl_choice.grid(row=0, column=0, padx=10, pady=10)
rad_white.grid(row=1, column=0, padx=10, pady=10)
rad_yellow.grid(row=2, column=0, padx=10, pady=10)
rad_red.grid(row=3, column=0, padx=10, pady=10)

# размещение элементов в главном окне
lbl_start.grid(row=0, column=3, padx=10, pady=10)
frm_right.grid(row=1, column=4, padx=10, pady=10)
frm_left.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()
