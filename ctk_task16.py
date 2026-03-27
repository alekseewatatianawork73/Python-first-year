import customtkinter as ctk


def temperature(t):
    t = int(t)
    lbl_temp.configure(text=f'Температура: {t}°C')
    if -20 <= t < 0:
        lbl_frm.configure(text='ХОЛОДНО')
        frm_temp.configure(fg_color='cyan')
    elif 0 <= t < 20:
        lbl_frm.configure(text='ТЕПЛО')
        frm_temp.configure(fg_color='darkgoldenrod1')
    else:
        lbl_frm.configure(text='ЖАРКО')
        frm_temp.configure(fg_color='orangered')


root = ctk.CTk()
root.title("Приложение-Термометр")
root.geometry("1200x700")
root.configure(fg_color='bisque')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Times New Roman', size=25, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Термометр', font=my_font)

lbl_temp = ctk.CTkLabel(master=root)
lbl_temp.configure(text='Температура: 0°C', font=my_font)

sl = ctk.CTkSlider(master=root)
sl.configure(from_=-20, to=40, fg_color='gray', progress_color='darkcyan', button_color='bisque3',
             button_hover_color='bisque4', width=500, command=temperature)
sl.set(0)

frm_temp = ctk.CTkFrame(master=root, width=500, height=300)
frm_temp.configure(border_width=3, corner_radius=30, border_color='bisque4', fg_color='darkgoldenrod1')
frm_temp.grid_propagate(False)

lbl_frm = ctk.CTkLabel(master=frm_temp)
lbl_frm.configure(text='ТЕПЛО', font=my_font)

frm_temp.columnconfigure(0, weight=1)
frm_temp.rowconfigure(0, weight=1)
lbl_frm.grid(row=0, column=0)

lbl_start.grid(row=0, column=3, padx=10, pady=10)
lbl_temp.grid(row=1, column=3, padx=10, pady=10)
sl.grid(row=2, column=3, padx=10, pady=10)
frm_temp.grid(row=3, column=3, padx=10, pady=10)

root.mainloop()
