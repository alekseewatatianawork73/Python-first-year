import customtkinter as ctk


def press():
    side1 = int(entr1.get())
    side2 = int(entr2.get())
    square = side1 * side2
    entr_res.configure(state='normal')
    entr_res.delete(0, 'end')
    entr_res.insert(0, str(square))
    entr_res.configure(state='disabled')


root = ctk.CTk()
root.geometry('1000x500')
root.title('Площадь прямоугольника')
root.configure(fg_color='peachpuff')

r, c = 7, 7
for i in range(r):
    root.rowconfigure(i, weight=1)
for i in range(c):
    root.columnconfigure(i, weight=1)

my_font = font=ctk.CTkFont(family='Courier', size=20, weight='bold')

btn = ctk.CTkButton(master=root)
btn.configure(text='Найти площадь', command=press, font=my_font, fg_color='chocolate', text_color='white')
btn.grid(row=3, column=3, padx=20, pady=20, sticky='ew')

lbl = ctk.CTkLabel(master=root)
lbl.configure(text='Поиск площади прямоугольника', font=my_font)
lbl.grid(row=0, column=3, padx=20, pady=20, sticky='ew')

entr1 = ctk.CTkEntry(master=root)
entr1.configure(justify='center', state='normal', font=my_font)
entr1.grid(row=1, column=2, padx=20, pady=20, sticky='ns')

entr2 = ctk.CTkEntry(master=root)
entr2.configure(justify='center', state='normal', font=my_font)
entr2.grid(row=1, column=3, padx=20, pady=20, sticky='ns')

entr_res = ctk.CTkEntry(master=root)
entr_res.configure(justify='center', state='disabled', font=my_font)
entr_res.grid(row=1, column=4, padx=20, pady=20, sticky='nsew')

root.mainloop()
