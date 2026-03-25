import customtkinter as ctk


def press():
    switches = [sw_light, sw_wifi, sw_blue]
    count = 0
    for sw in switches:
        if sw.get():
            count += 1
    lbl_res.configure(text=f'Активно устройств: {count} из 3')


root = ctk.CTk()
root.title("Панель управления устройствами")
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
lbl_start.configure(text='Управление устройствами', font=my_font)

sw_light = ctk.CTkSwitch(master=root)
sw_light.configure(text='Подсветка', font=mini_font, state='normal', fg_color='gray',
             button_color='green', progress_color='lightgreen', button_hover_color='darkgreen', command=press)

sw_wifi = ctk.CTkSwitch(master=root)
sw_wifi.configure(text='Wi-Fi', font=mini_font, state='normal', fg_color='gray',
             button_color='green', progress_color='lightgreen', button_hover_color='darkgreen', command=press)

sw_blue = ctk.CTkSwitch(master=root)
sw_blue.configure(text='Bluetooth', font=mini_font, state='normal', fg_color='gray',
             button_color='green', progress_color='lightgreen', button_hover_color='darkgreen', command=press)

lbl_res = ctk.CTkLabel(master=root)
lbl_res.configure(text='Активно устройств: 0 из 3', font=my_font)

# размещение элементов в главном окне
lbl_start.grid(row=0, column=3, padx=10, pady=10)
sw_light.grid(row=1, column=3, padx=10, pady=10)
sw_wifi.grid(row=2, column=3, padx=10, pady=10)
sw_blue.grid(row=3, column=3, padx=10, pady=10)
lbl_res.grid(row=4, column=3, padx=10, pady=10)

root.mainloop()
