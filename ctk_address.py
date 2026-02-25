import customtkinter as ctk


# функция для выпадающего списка со странами
def city_list(choice):
    # в зависимости от выбранной страны меняем список городов в списке cmb_city
    if choice == 'Россия':
        cmb_city.configure(values=["Москва", "Санкт-Петербург", "Ульяновск"])
    elif choice == 'Великобритания':
        cmb_city.configure(values=["Лондон", "Уэльс", "Эдинбург"])
    else:
        cmb_city.configure(values=["Париж", "Марсель", "Авиньон"])


# кнопка для просмотра результата
def press_res():
    # получаем значения страны и города из выпадающих списков
    country, city = cmb_country.get(), cmb_city.get()
    # получаем адрес из текстового поля entr_address
    addr = entr_address.get()
    # берём внешнюю (глобальную) переменную my_address и записываем в неё готовый адрес
    global my_address  # указываем, что переменная создана не внутри этой функции, а снаружи, в основной программе
    my_address += country + ', г. ' + city + ', ' + addr
    lbl_res.configure(text=my_address)  # заносим адрес в текстовую метку lbl_res
    # удаляем все виджеты на экране (полностью очищаем окно)
    for widget in root.winfo_children():
        widget.grid_forget()
    # отображаем только lbl_res
    lbl_res.grid(row=3, column=3, padx=10, pady=10)


# создание главного окна
root = ctk.CTk()
root.title("Место проживания")
root.geometry("1000x500")
root.configure(fg_color='salmon')

# сетка 7х7 для размещения виджетов
rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=20)

# формируем надписи
lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text="Выберите место проживания:", font=my_font)

lbl_country = ctk.CTkLabel(master=root)
lbl_country.configure(text="Выберите страну:", font=my_font)

lbl_city = ctk.CTkLabel(master=root)
lbl_city.configure(text="Выберите город:", font=my_font)

lbl_address = ctk.CTkLabel(master=root)
lbl_address.configure(text="Введите адрес проживания:", font=my_font)

my_address = "Ваше место проживания: "
lbl_res = ctk.CTkLabel(master=root)
lbl_res.configure(text=my_address + '\nМожете закрыть окно', font=my_font)

# выпадающий список для выбора страны
countries = ["Россия", "Великобритания", "Франция"]
cmb_country = ctk.CTkComboBox(master=root)
cmb_country.configure(justify="center", values=countries, state="readonly", font=my_font, command=city_list)
cmb_country.set('...')

# выпадающий список для выбора города (пока пустой, потому что не выбрана страна)
cities = []
cmb_city = ctk.CTkComboBox(master=root)
cmb_city.configure(justify="center", values=cities, state="readonly", font=my_font)
cmb_city.set('...')

# текстовое поле для ввода адреса
entr_address = ctk.CTkEntry(master=root)
entr_address.configure(justify='center', font=my_font, state='normal')

# кнопка для просмотра результата
btn_result = ctk.CTkButton(master=root)
btn_result.configure(text="Готово!", command=press_res, font=my_font, fg_color='red3', hover_color='red4')

# размещение элементов в окне
lbl_start.grid(row=0, column=3, padx=10, pady=10)

lbl_country.grid(row=1, column=2, padx=10, pady=10)
lbl_city.grid(row=1, column=3, padx=10, pady=10)
lbl_address.grid(row=1, column=4, padx=10, pady=10)

cmb_country.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
cmb_city.grid(row=2, column=3, padx=10, pady=10, sticky='ew')
entr_address.grid(row=2, column=4, padx=10, pady=10, sticky='ns')

btn_result.grid(row=3, column=3, padx=10, pady=10, sticky='ew')

root.mainloop()
