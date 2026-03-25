import customtkinter as ctk


def rgb_color(value):
    r = int(sl_red.get())
    g = int(sl_green.get())
    b = int(sl_blue.get())
    frm_res.configure(fg_color=f'#{r:02x}{g:02x}{b:02x}')
    lbl_res.configure(text=f'Выбранный цвет в формате RGB: ({r}, {g}, {b})')


root = ctk.CTk()
root.title("Цветовой миксер")
root.geometry("1200x700")
root.configure(fg_color='cornsilk')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=35, weight='bold')
mini_font = ctk.CTkFont(family='Times New Roman', size=25, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Подбираем цвет в формате RGB', font=my_font)

frm_sl = ctk.CTkFrame(master=root, width=500, height=200)
frm_sl.configure(border_width=3, corner_radius=20, fg_color='cornsilk2')
frm_sl.grid_propagate(False)

sl_red = ctk.CTkSlider(master=frm_sl)
sl_red.configure(from_=0, to=255, fg_color='gray', progress_color='orange', button_color='red',
             button_hover_color='darkred', width=200, command=rgb_color)
sl_red.set(0)

sl_green = ctk.CTkSlider(master=frm_sl)
sl_green.configure(from_=0, to=255, fg_color='gray', progress_color='orange', button_color='red',
             button_hover_color='darkred', width=200, command=rgb_color)
sl_green.set(0)

sl_blue = ctk.CTkSlider(master=frm_sl)
sl_blue.configure(from_=0, to=255, fg_color='gray', progress_color='orange', button_color='red',
             button_hover_color='darkred', width=200, command=rgb_color)
sl_blue.set(0)

frm_sl.rowconfigure(index=(0, 1, 2), weight=1)
frm_sl.columnconfigure(index=(0, 1), weight=1)
sl_red.grid(row=0, column=1, padx=10, pady=10)
sl_green.grid(row=1, column=1, padx=10, pady=10)
sl_blue.grid(row=2, column=1, padx=10, pady=10)

colors = ['Красный:', 'Зеленый:', 'Синий:']
for i in range(3):
    lbl = ctk.CTkLabel(master=frm_sl)
    lbl.configure(text=colors[i], font=mini_font)
    lbl.grid(row=i, column=0, padx=10, pady=10)

lbl_res = ctk.CTkLabel(master=root)
lbl_res.configure(text='Выбранный цвет в формате RGB: (0, 0, 0)', font=mini_font)

frm_res = ctk.CTkFrame(master=root, width=500, height=200)
frm_res.configure(border_width=3, corner_radius=20, fg_color='black')
frm_res.grid_propagate(False)

lbl_start.grid(row=0, column=3, padx=10, pady=10)
frm_sl.grid(row=1, column=3, padx=10, pady=10)
lbl_res.grid(row=2, column=3, padx=10, pady=10)
frm_res.grid(row=3, column=3, padx=10, pady=10)

root.mainloop()
