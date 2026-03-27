import customtkinter as ctk


def calc_tips(s):
    lbl_tips.configure(text=f'Чаевые: {int(s)}%')


def get_tips():
    start_sum = int(entr_sum.get())
    tips = int(sl_tips.get())
    tips_sum = start_sum // 100 * tips
    total_sum = start_sum + tips_sum
    lbl_res1.configure(text=f'Чаевые: {tips_sum} руб.')
    lbl_res2.configure(text=f'Итого: {total_sum} руб.')


root = ctk.CTk()
root.title("Калькулятор чаевых")
root.geometry("1200x700")
root.configure(fg_color='darkseagreen1')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=25, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Расчёт чаевых', font=my_font)

lbl_sum = ctk.CTkLabel(master=root)
lbl_sum.configure(text='Сумма счёта (в рублях):', font=my_font)

entr_sum = ctk.CTkEntry(master=root)
entr_sum.configure(font=my_font, justify='center')

lbl_tips = ctk.CTkLabel(master=root)
lbl_tips.configure(text='Чаевые: 0%', font=my_font)

sl_tips = ctk.CTkSlider(master=root)
sl_tips.configure(from_=0, to=50, fg_color='gray', progress_color='darkolivegreen4', button_color='forestgreen',
             button_hover_color='darkseagreen4', width=300, command=calc_tips)
sl_tips.set(0)

btn = ctk.CTkButton(master=root)
btn.configure(text="Рассчитать чаевые", font=my_font, command=get_tips, fg_color='forestgreen', hover_color='darkseagreen4')
btn.grid(row=4, column=3, padx=20, pady=20, sticky="nsew")

frm_res = ctk.CTkFrame(master=root, width=500, height=300)
frm_res.configure(border_width=3, corner_radius=30, border_color='forestgreen', fg_color='darkolivegreen1')
frm_res.grid_propagate(False)

lbl_res1 = ctk.CTkLabel(master=frm_res)
lbl_res1.configure(text='Чаевые: 0 руб.', font=my_font)

lbl_res2 = ctk.CTkLabel(master=frm_res)
lbl_res2.configure(text='Итого: 0 руб.', font=my_font)

frm_res.columnconfigure(0, weight=1)
frm_res.rowconfigure((0, 1), weight=1)
lbl_res1.grid(row=0, column=0, padx=10, pady=10)
lbl_res2.grid(row=1, column=0, padx=10, pady=10)

lbl_start.grid(row=0, column=3, padx=10, pady=10)
lbl_sum.grid(row=1, column=2, padx=10, pady=10)
lbl_tips.grid(row=1, column=4, padx=10, pady=10)
entr_sum.grid(row=2, column=2, padx=10, pady=10, sticky='ew')
sl_tips.grid(row=2, column=4, padx=10, pady=10)
btn.grid(row=3, column=3, padx=10, pady=10)
frm_res.grid(row=4, column=3, padx=10, pady=10)

root.mainloop()
