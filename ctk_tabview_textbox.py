import customtkinter as ctk


# функция для смены цвета фона
def theme():
    if sw.get():
        tbw.configure(fg_color='red')
    else:
        tbw.configure(fg_color='aquamarine')


# функция для отображения информации о программе в текстовом поле txt
def show_inf():
    my_text = 'Здесь должна быть расположена информация о программе. Чтобы скрыть информацию, нажмите на кнопку.'
    txt.configure(state='normal')
    txt.delete('0.0', 'end')  # очищаем текстовое поле
    txt.insert('0.0', my_text)  # вставляем текст my_text в текстовое поле
    txt.configure(state='disabled')


# функция для удаления информации о программе из текстового поля txt
def del_inf():
    txt.configure(state='normal')
    txt.delete('0.0', 'end')
    txt.configure(state='disabled')


# основная программа
root = ctk.CTk()
root.title('Вкладки и большие текстовые поля')
root.geometry("1000x700")

# сетка для размещения элементов в главном окне root
rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

# шрифты
mini_font = ctk.CTkFont(family='Courier', size=20, weight='bold')
my_font = ctk.CTkFont(family='Courier', size=25, weight='bold')
big_font = ctk.CTkFont(family='Courier', size=30, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Приложение со вкладками', font=big_font)

# создаём панель вкладок при помощи класса CTkTabview
tbw = ctk.CTkTabview(master=root)
tbw.configure(width=900, height=500, fg_color='aquamarine', border_width=3, border_color='black',
              segmented_button_selected_color='aquamarine', segmented_button_unselected_color='aquamarine3',
              text_color='black', segmented_button_selected_hover_color='gray',
              segmented_button_unselected_hover_color='gray', segmented_button_fg_color='black')
tbw._segmented_button.configure(font=mini_font) # задаём шрифт названиям вкладок
tbw.grid_propagate(False)  # запрещаем изменяться размерам окна вкладок

# добавляем на нашу панель три новые вкладки
tbw.add('Главная')
tbw.add('Настройки')
tbw.add('О программе')

# вкладка "Главная" - сохраняем её в переменную при помощи метода tab("название вкладки")
main_tbw = tbw.tab('Главная')

# виджеты во вкладке "Главная"
lbl_main = ctk.CTkLabel(master=main_tbw)
lbl_main.configure(text='Добро пожаловать в приложение со вкладками!\nВы находитесь внутри первой вкладки.\nЭто главная страница.', font=my_font)

# сетка и размещение элементов во вкладке "Главная"
main_tbw.rowconfigure(index=0, weight=1)
main_tbw.columnconfigure(index=0, weight=1)
lbl_main.grid(row=0, column=0, padx=10, pady=10)

# вкладка "Настройки"
setting_tbw = tbw.tab('Настройки')

# виджеты во вкладке "Настройки"
lbl_setting = ctk.CTkLabel(master=setting_tbw)
lbl_setting.configure(text='Настройки', font=big_font)

sw = ctk.CTkSwitch(master=setting_tbw)
sw.configure(text='Включить красный фон', font=my_font, command=theme)

# сетка и размещение элементов во вкладке "Настройки"
setting_tbw.rowconfigure(index=(0, 1), weight=1)
setting_tbw.columnconfigure(index=0, weight=1)
lbl_setting.grid(row=0, column=0, padx=10, pady=10)
sw.grid(row=1, column=0, padx=10, pady=10)

# вкладка "О программе"
prog_tbw = tbw.tab('О программе')

# виджеты во вкладке "О программе"
lbl_prog = ctk.CTkLabel(master=prog_tbw)
lbl_prog.configure(text='О программе', font=big_font)

# создадим в этой вкладке большое текстовое поле при помощи класса CTkTextBox()
txt = ctk.CTkTextbox(master=prog_tbw)
txt.configure(font=my_font, wrap='word', width=500, height=200, state='disabled', border_width=3, border_color='darkgreen')

btn_show = ctk.CTkButton(master=prog_tbw)
btn_show.configure(text="Показать информацию", font=my_font, fg_color='darkgreen', command=show_inf)

btn_del = ctk.CTkButton(master=prog_tbw)
btn_del.configure(text="Скрыть информацию", font=my_font, fg_color='darkgreen', command=del_inf)

# сетка и размещение элементов во вкладке "О программе"
prog_tbw.rowconfigure(index=(0, 1, 2, 3), weight=1)
prog_tbw.columnconfigure(index=0, weight=1)
lbl_prog.grid(row=0, column=0, padx=10, pady=10)
txt.grid(row=1, column=0, padx=10, pady=10)
btn_show.grid(row=2, column=0, padx=10, pady=10)
btn_del.grid(row=3, column=0, padx=10, pady=10)

# размещение элементов в главном окне root
lbl_start.grid(row=0, column=3, padx=10, pady=10)
tbw.grid(row=1, column=3, padx=10, pady=10)

root.mainloop()
