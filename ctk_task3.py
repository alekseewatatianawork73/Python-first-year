import customtkinter as ctk


def check():
    p = entr_pass.get()
    res = 'слабый'
    count_up, count_dig = 0, 0
    for x in p:
        if x.isupper():
            count_up += 1
        if x.isdigit():
            count_dig += 1
    if len(p) >= 5 and count_dig > 0 and count_up > 0:
        res = 'надёжный'
    entr_res.configure(state='normal')
    entr_res.delete(0, 'end')
    entr_res.insert(0, res)
    entr_res.configure(state='disabled')


root = ctk.CTk()
root.geometry('1000x500')
root.title('Проверка пароля')
root.configure(fg_color='darkseagreen1')

r, c = 7, 7
for i in range(r):
    root.rowconfigure(i, weight=1)
for i in range(c):
    root.columnconfigure(i, weight=1)

my_font = font=ctk.CTkFont(family='Courier', size=20, weight='bold')

btn = ctk.CTkButton(master=root)
btn.configure(text='Проверить пароль', command=check, font=my_font, fg_color='forestgreen', text_color='white')
btn.grid(row=3, column=3, padx=20, pady=20, sticky='ew')

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Надёжен ли пароль?', font=my_font)
lbl.grid(row=0, column=3, padx=20, pady=20)

lbl_pass = ctk.CTkLabel(master=root)
lbl_pass.configure(text='Введите ваш пароль:', font=my_font)
lbl_pass.grid(row=1, column=2, padx=20, pady=20)

lbl_res = ctk.CTkLabel(master=root)
lbl_res.configure(text='Результат проверки:', font=my_font)
lbl_res.grid(row=1, column=4, padx=20, pady=20)

entr_pass = ctk.CTkEntry(master=root)
entr_pass.configure(justify='center', state='normal', font=my_font)
entr_pass.grid(row=2, column=2, padx=20, pady=20, sticky='ew')

entr_res = ctk.CTkEntry(master=root)
entr_res.configure(justify='center', state='disabled', font=my_font)
entr_res.grid(row=2, column=4, padx=20, pady=20, sticky='ew')

root.mainloop()
