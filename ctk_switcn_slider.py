import customtkinter as ctk

# функция, срабатывающая при нажатии на переключатель
def on_sound():
    # получим значение переключателя: True - включен или False - выключен
    sound = sw.get()
    if sound:  # вместо "sound == True" можно писать просто "sound"
        lbl_sound.configure(text='Звук включен')
    else:
        lbl_sound.configure(text='Звук выключен')


# функция, срабатывающая при изменении значения ползунка (value - значение ползунка)
def volume(value):
    # значение ползунка поменялось => меняем значение громкости в надписи
    lbl_volume.configure(text=f'Громкость: {int(value)}')


# основная программа
# главное окно root
root = ctk.CTk()
root.title("Новые виджеты")
root.geometry("1200x700")

# сетка для главного окна: 7 строк и 7 столбцов
rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=25, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Переключатель и ползунок', font=my_font)

lbl_sw = ctk.CTkLabel(master=root)
lbl_sw.configure(text='Переключатель:', font=my_font)

# создаём переключатель и задаём свойства
sw = ctk.CTkSwitch(master=root)
sw.configure(text='Включить звук', font=my_font, state='normal', fg_color='gray',
             button_color='green', progress_color='lightgreen', button_hover_color='darkgreen', command=on_sound)

lbl_sl = ctk.CTkLabel(master=root)
lbl_sl.configure(text='Ползунок:', font=my_font)

# создаём слайдер (ползунок) и задаём свойства
sl = ctk.CTkSlider(master=root)
sl.configure(from_=0, to=100, number_of_steps=10, state='normal', fg_color='gray',
             progress_color='orange', button_color='red', button_hover_color='darkred', width=500, command=volume)
sl.set(0)  # устанавливаем начальное значение 0

lbl_sound = ctk.CTkLabel(master=root)
lbl_sound.configure(text='Звук выключен', font=my_font, text_color='green')

lbl_volume = ctk.CTkLabel(master=root)
lbl_volume.configure(text='Громкость: 0', font=my_font, text_color='red')

# размещение элементов в главном окне
lbl_start.grid(row=0, column=3, padx=10, pady=10)
lbl_sw.grid(row=1, column=3, padx=10, pady=10)
sw.grid(row=2, column=3, padx=10, pady=10)
lbl_sl.grid(row=3, column=3, padx=10, pady=10)
sl.grid(row=4, column=3, padx=10, pady=10)
lbl_sound.grid(row=5, column=2, padx=10, pady=10)
lbl_volume.grid(row=5, column=4, padx=10, pady=10)

root.mainloop()
