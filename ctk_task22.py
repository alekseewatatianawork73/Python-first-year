import customtkinter as ctk

my_text = None


def sending():
    global my_text
    my_text = txt_send.get('0.0', 'end')
    txt_send.delete('0.0', 'end')
    txt_get.configure(state='normal')
    txt_get.delete('0.0', 'end')
    txt_get.insert('0.0', 'У Вас новое сообщение!')
    txt_get.configure(state='disabled')


def show_inf():
    global my_text
    if my_text:
        txt_get.configure(state='normal')
        txt_get.delete('0.0', 'end')
        txt_get.insert('0.0', my_text)
        txt_get.configure(state='disabled')


def del_inf():
    txt_get.configure(state='normal')
    txt_get.delete('0.0', 'end')
    txt_get.configure(state='disabled')


# основная программа
root = ctk.CTk()
root.title('Обмен информацией')
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
lbl_start.configure(text='Обмен информацией между вкладками', font=big_font)

# создаём панель вкладок при помощи класса CTkTabview
tbw = ctk.CTkTabview(master=root)
tbw.configure(width=900, height=500, fg_color='aquamarine', border_width=3, border_color='black',
              segmented_button_selected_color='aquamarine', segmented_button_unselected_color='aquamarine3',
              text_color='black', segmented_button_selected_hover_color='gray',
              segmented_button_unselected_hover_color='gray', segmented_button_fg_color='black')
tbw._segmented_button.configure(font=mini_font) # задаём шрифт названиям вкладок
tbw.grid_propagate(False)  # запрещаем изменяться размерам окна вкладок

# добавляем на нашу панель три новые вкладки
tbw.add('Отправитель')
tbw.add('Получатель')

send_tbw = tbw.tab('Отправитель')

# виджеты во вкладке "Главная"
lbl_send = ctk.CTkLabel(master=send_tbw)
lbl_send.configure(text='Введите сообщение:', font=my_font)

txt_send = ctk.CTkTextbox(master=send_tbw)
txt_send.configure(font=my_font, wrap='word', width=500, height=200, border_width=3, border_color='darkgreen')

btn_send = ctk.CTkButton(master=send_tbw)
btn_send.configure(text="Отправить", font=my_font, fg_color='darkgreen', command=sending)

send_tbw.rowconfigure(index=(0, 1, 2), weight=1)
send_tbw.columnconfigure(index=0, weight=1)
lbl_send.grid(row=0, column=0, padx=10, pady=10)
txt_send.grid(row=1, column=0, padx=10, pady=10)
btn_send.grid(row=2, column=0, padx=10, pady=10)

get_tbw = tbw.tab('Получатель')

lbl_get = ctk.CTkLabel(master=get_tbw)
lbl_get.configure(text='Новое сообщение:', font=big_font)

txt_get = ctk.CTkTextbox(master=get_tbw)
txt_get.configure(font=my_font, wrap='word', state='disabled', width=500, height=200, border_width=3, border_color='darkgreen')

btn_show = ctk.CTkButton(master=get_tbw)
btn_show.configure(text="Показать сообщение", font=my_font, fg_color='darkgreen', command=show_inf)

btn_del = ctk.CTkButton(master=get_tbw)
btn_del.configure(text="Очистить поле", font=my_font, fg_color='darkgreen', command=del_inf)

get_tbw.rowconfigure(index=(0, 1, 2, 3), weight=1)
get_tbw.columnconfigure(index=0, weight=1)
lbl_get.grid(row=0, column=0, padx=10, pady=10)
txt_get.grid(row=1, column=0, padx=10, pady=10)
btn_show.grid(row=2, column=0, padx=10, pady=10)
btn_del.grid(row=3, column=0, padx=10, pady=10)

# размещение элементов в главном окне root
lbl_start.grid(row=0, column=3, padx=10, pady=10)
tbw.grid(row=1, column=3, padx=10, pady=10)

root.mainloop()
