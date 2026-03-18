import customtkinter as ctk

# глобальные переменные: размер шрифта, тема фона, наличие подсказок, наличие открытого окна настроек
font_size = 'Большой'
theme = 'dark'
tips = 'открыты'
window = None

# глобальные переменные для виджетов (чтобы их было видно во всех функциях)
var = None
ch_tip = None
cmb_font = None


def save():
    global font_size, theme, tips, var, ch_tip, cmb_font, window
    theme = var.get()
    if ch_tip.get():
        tips = 'открыты'
    else:
        tips = 'закрыты'
    font_size = cmb_font.get()

    ctk.set_appearance_mode(theme)
    if font_size == 'Маленький':
        my_font.configure(size=15)
    elif font_size == 'Средний':
        my_font.configure(size=20)
    else:
        my_font.configure(size=25)

    lbl_res.configure(text=f'Тема: {theme}, подсказки: {tips}, шрифт: {font_size}')
    window.destroy()


def cancel():
    global window
    window.destroy()


def settings():
    global window, var, ch_tip, cmb_font, font_size, theme, tips
    if window:
        window.destroy()

    window = ctk.CTkToplevel(master=root)
    window.title('Настройки')
    window.geometry('700x500')
    window.resizable(False, False)
    window.attributes('-topmost', True)

    lbl_theme = ctk.CTkLabel(master=window)
    lbl_theme.configure(text='Выберите тему фона:', font=my_font)

    var = ctk.StringVar(value=theme)
    rd_dark = ctk.CTkRadioButton(master=window, value='dark')
    rd_dark.configure(variable=var, text='Тёмная тема', font=my_font)
    rd_light = ctk.CTkRadioButton(master=window, value='light')
    rd_light.configure(variable=var, text='Светлая тема', font=my_font)

    lbl_tips = ctk.CTkLabel(master=window)
    lbl_tips.configure(text='Подсказки:', font=my_font)

    ch_tip = ctk.CTkCheckBox(master=window)
    ch_tip.configure(text='Открыть подсказки', font=my_font)
    if tips == 'открыты':
        ch_tip.select()

    lbl_font = ctk.CTkLabel(master=window)
    lbl_font.configure(text='Выберите размер шрифта:', font=my_font)

    cmb_font = ctk.CTkComboBox(master=window)
    cmb_font.configure(values=['Маленький', 'Средний', 'Большой'], font=my_font, justify='center')
    cmb_font.set(font_size)

    btn_save = ctk.CTkButton(master=window)
    btn_save.configure(text="Сохранить", font=my_font, command=save)

    btn_canc = ctk.CTkButton(master=window)
    btn_canc.configure(text="Отмена", font=my_font, command=cancel)

    lbl_theme.grid(row=0, column=0, padx=10, pady=10)
    rd_light.grid(row=0, column=1, padx=10, pady=10)
    rd_dark.grid(row=1, column=1, padx=10, pady=10)
    lbl_tips.grid(row=2, column=0, padx=10, pady=10)
    ch_tip.grid(row=2, column=1, padx=10, pady=10)
    lbl_font.grid(row=3, column=0, padx=10, pady=10)
    cmb_font.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
    btn_save.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    btn_canc.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='ew')



# основная программа
ctk.set_appearance_mode(theme)

root = ctk.CTk()
root.title("Окно настроек")
root.geometry("1000x700")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=25, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Окно с настройками', font=my_font)

frm = ctk.CTkFrame(master=root, width=500, height=200)
frm.configure(border_color='gray25', border_width=3, corner_radius=30)
frm.grid_propagate(False)

lbl_res = ctk.CTkLabel(master=frm)
lbl_res.configure(text='Текущие настройки: по умолчанию', font=my_font)

btn_set = ctk.CTkButton(master=root)
btn_set.configure(text="Открыть настройки", font=my_font, command=settings)

frm.columnconfigure(index=0, weight=1)
frm.rowconfigure(index=0, weight=1)
lbl_res.grid(row=0, column=0, padx=10, pady=10)

# размещение элементов в основном окне
lbl_start.grid(row=0, column=3, padx=10, pady=10)
frm.grid(row=1, column=3, padx=10, pady=10)
btn_set.grid(row=2, column=3, padx=10, pady=10, sticky='nsew')

root.mainloop()
