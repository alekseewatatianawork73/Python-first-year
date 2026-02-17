import customtkinter as ctk


def press():
    a = float(entr_from.get())
    val1, val2 = cmb_from.get(), cmb_to.get()
    res = 0
    if val1 == 'килограммы' and val2 == 'фунты':
        res = a * 2.2
    elif val1 == 'фунты' and val2 == 'килограммы':
        res = a / 2.2
    elif val1 == 'метры' and val2 == 'футы':
        res = a * 3.28
    elif val1 == 'футы' and val2 == 'метры':
        res = a / 3.28
    elif val1 == val2:
        res = a
    else:
        res = 'Невозможно!'
    entr_to.configure(state='normal')
    entr_to.delete(0, 'end')
    entr_to.insert(0, str(res))
    entr_to.configure(state='disabled')


root = ctk.CTk()
root.title("Конвертер величин измерения")
root.geometry("1000x500")
root.configure(fg_color='darkseagreen1')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=20)

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text="Выберите величины измерения:", font=my_font)

lbl_from = ctk.CTkLabel(master=root)
lbl_from.configure(text="Из чего?", font=my_font)

lbl_to = ctk.CTkLabel(master=root)
lbl_to.configure(text="Во что?", font=my_font)

colors = ["килограммы", "фунты", "метры", "футы"]
cmb_from = ctk.CTkComboBox(master=root)
cmb_from.configure(justify="center", values=colors, state="readonly", font=my_font)
cmb_from.set("килограммы")

cmb_to = ctk.CTkComboBox(master=root)
cmb_to.configure(justify="center", values=colors, state="readonly", font=my_font)
cmb_to.set("килограммы")

entr_from = ctk.CTkEntry(master=root)
entr_from.configure(justify='center', font=my_font, state='normal')

entr_to = ctk.CTkEntry(master=root)
entr_to.configure(justify='center', font=my_font, state='disabled')

btn_result = ctk.CTkButton(master=root)
btn_result.configure(text="Перевести", command=press, font=my_font, fg_color='darkgreen', hover_color='darkolivegreen')

lbl_start.grid(row=0, column=3, padx=10, pady=10)
lbl_from.grid(row=1, column=2, padx=10, pady=10)
lbl_to.grid(row=1, column=4, padx=10, pady=10)
cmb_from.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
cmb_to.grid(row=2, column=4, padx=10, pady=10, sticky='ew')
entr_from.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')
entr_to.grid(row=3, column=4, padx=10, pady=10, sticky='nsew')
btn_result.grid(row=4, column=3, padx=10, pady=10, sticky='ew')

root.mainloop()
