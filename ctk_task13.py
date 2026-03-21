import customtkinter as ctk


def figure():
    fig = rad_var.get()
    if fig == 1:
        lbl_fig.configure(text="🔴")
    elif fig == 2:
        lbl_fig.configure(text="🟦")
    else:
        lbl_fig.configure(text="⭐")


def frm_color(color):
    if color == 'Белый':
        frm_res.configure(fg_color='white')
    elif color == 'Зеленый':
        frm_res.configure(fg_color='lightgreen')
    else:
        frm_res.configure(fg_color='lightyellow')


# основная программа
root = ctk.CTk()
root.title("Два фрейма - один выбор")
root.geometry("1200x700")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=25, weight='bold')
font_fig = ctk.CTkFont(size=70)

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Выбор фигуры', font=my_font)

frm_choice = ctk.CTkFrame(master=root, width=400, height=500)
frm_choice.configure(border_width=3, corner_radius=30)
frm_choice.grid_propagate(False)

lbl_color = ctk.CTkLabel(master=frm_choice)
lbl_color.configure(text='Выберите цвет фона: ', font=my_font)

cmb_color = ctk.CTkComboBox(master=frm_choice)
cmb_color.configure(values=['Белый', 'Зеленый', 'Желтый'], font=my_font, justify='center', command=frm_color)
cmb_color.set('Белый')

lbl_choice = ctk.CTkLabel(master=frm_choice)
lbl_choice.configure(text='Выберите фигуру: ', font=my_font)

rad_var = ctk.IntVar(value=1)
rad_circle = ctk.CTkRadioButton(master=frm_choice, value=1)
rad_circle.configure(text='Круг', font=my_font, command=figure, variable=rad_var)
rad_square = ctk.CTkRadioButton(master=frm_choice, value=2)
rad_square.configure(text='Квадрат', font=my_font, command=figure, variable=rad_var)
rad_star = ctk.CTkRadioButton(master=frm_choice, value=3)
rad_star.configure(text='Звезда', font=my_font, command=figure, variable=rad_var)

frm_choice.columnconfigure(index=0, weight=1)
frm_choice.rowconfigure(index=(0, 1, 2, 3, 4, 5), weight=1)
lbl_color.grid(row=0, column=0, padx=10, pady=10)
cmb_color.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
lbl_choice.grid(row=2, column=0, padx=10, pady=10)
rad_circle.grid(row=3, column=0, padx=10, pady=10)
rad_square.grid(row=4, column=0, padx=10, pady=10)
rad_star.grid(row=5, column=0, padx=10, pady=10)

frm_res = ctk.CTkFrame(master=root, width=400, height=500)
frm_res.configure(border_width=3, corner_radius=30)
frm_res.grid_propagate(False)

lbl_res = ctk.CTkLabel(master=frm_res)
lbl_res.configure(text='Результат:', font=my_font)

lbl_fig = ctk.CTkLabel(master=frm_res)
lbl_fig.configure(text="🔴", font=font_fig)

frm_res.columnconfigure(index=0, weight=1)
frm_res.rowconfigure(index=(0, 1), weight=1)
lbl_res.grid(row=0, column=0, padx=10, pady=10)
lbl_fig.grid(row=1, column=0, padx=10, pady=10)

# размещение элементов в основном окне
lbl_start.grid(row=0, column=3, padx=10, pady=10)
frm_choice.grid(row=1, column=2, padx=10, pady=10)
frm_res.grid(row=1, column=4, padx=10, pady=10)

root.mainloop()
