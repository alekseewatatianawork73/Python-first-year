import customtkinter as ctk


def press():
    fon, but1, but2 = 'darkseagreen1', 'darkgreen', 'darkolivegreen'
    text = 'white'
    if cmb.get() == "Синий":
        fon, but1, but2 = 'lightcyan', 'navyblue', 'royalblue'
    elif cmb.get() == "Жёлтый":
        fon, but1, but2 = 'lightyellow', 'goldenrod', 'gold'
        text = 'black'
    root.configure(fg_color=fon)
    btn_result.configure(text="Сменить оформление", command=press, font=my_font, fg_color=but1, hover_color=but2, text_color=text)


root = ctk.CTk()
root.title("Цветное окно")
root.geometry("1000x500")
root.configure(fg_color='darkseagreen1')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=20)

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text="Приложение с выпадающим списком", font=my_font)

lbl_cmb = ctk.CTkLabel(master=root)
lbl_cmb.configure(text="Выберите цветовое оформление:", font=my_font)

colors = ["Зелёный", "Жёлтый", "Синий"]
cmb = ctk.CTkComboBox(master=root)
cmb.configure(justify="center", values=colors, state="readonly", font=my_font)
cmb.set("Зелёный")

btn_result = ctk.CTkButton(master=root)
btn_result.configure(text="Сменить оформление", command=press, font=my_font, fg_color='darkgreen', hover_color='darkolivegreen')

lbl_start.grid(row=0, column=3, padx=10, pady=10)
lbl_cmb.grid(row=1, column=3, padx=10, pady=10)
cmb.grid(row=2, column=3, padx=10, pady=10, sticky='ew')
btn_result.grid(row=3, column=3, padx=10, pady=10, sticky='ew')

root.mainloop()
