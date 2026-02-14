import customtkinter as ctk


def usd():
    rub = float(entr_rub.get())
    doll = round(rub / 77.19, 2)
    entr_res.configure(state='normal')
    entr_res.delete(0, 'end')
    entr_res.insert(0, str(doll))
    entr_res.configure(state='disabled')


def eur():
    rub = float(entr_rub.get())
    euro = round(rub / 91.56, 2)
    entr_res.configure(state='normal')
    entr_res.delete(0, 'end')
    entr_res.insert(0, str(euro))
    entr_res.configure(state='disabled')


root = ctk.CTk()
root.geometry('1000x500')
root.title('Конвертер валют')
root.configure(fg_color='peachpuff')

r, c = 7, 7
for i in range(r):
    root.rowconfigure(i, weight=1)
for i in range(c):
    root.columnconfigure(i, weight=1)

my_font = font=ctk.CTkFont(family='Courier', size=20, weight='bold')

btn_usd = ctk.CTkButton(master=root)
btn_usd.configure(text='Конвертировать в USD', command=usd, font=my_font, fg_color='chocolate', text_color='white')
btn_usd.grid(row=3, column=3, padx=20, pady=20, sticky='ew')

btn_eur = ctk.CTkButton(master=root)
btn_eur.configure(text='Конвертировать в EUR', command=eur, font=my_font, fg_color='chocolate', text_color='white')
btn_eur.grid(row=4, column=3, padx=20, pady=20, sticky='ew')

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Конвертация валюты', font=my_font)
lbl.grid(row=0, column=3, padx=20, pady=20)

lbl_rub = ctk.CTkLabel(master=root)
lbl_rub.configure(text='Сумма в рублях:', font=my_font)
lbl_rub.grid(row=1, column=2, padx=20, pady=20)

lbl_res = ctk.CTkLabel(master=root)
lbl_res.configure(text='Сумма в долларах/евро:', font=my_font)
lbl_res.grid(row=1, column=4, padx=20, pady=20)

entr_rub = ctk.CTkEntry(master=root)
entr_rub.configure(justify='center', state='normal', font=my_font)
entr_rub.grid(row=2, column=2, padx=20, pady=20, sticky='ns')

entr_res = ctk.CTkEntry(master=root)
entr_res.configure(justify='center', state='disabled', font=my_font)
entr_res.grid(row=2, column=4, padx=20, pady=20, sticky='ns')

root.mainloop()
