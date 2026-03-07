import customtkinter as ctk

root = ctk.CTk()
root.title("Кнопка 'Закрыть окно'")
root.geometry("1000x500")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=20)

btn = ctk.CTkButton(master=root)
# используем лямбда-функцию в параметре command, чтобы закрыть окно методом destroy()
btn.configure(text="Закрыть окно", font=my_font, command=lambda: root.destroy())
btn.grid(row=3, column=3, padx=10, pady=10, sticky='ew')

root.mainloop()
