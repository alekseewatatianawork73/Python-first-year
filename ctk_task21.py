import customtkinter as ctk
from pygame import mixer
mixer.init()

value = 0


def download():
    global value
    if value < 100:
        value += 1
        sl.set(value)
        lbl_frm.configure(text=f'Идёт загрузка: {value}%')
        root.after(200, download)
    else:
        value = 0
        lbl_frm.configure(text='Загрузка завершена!')
        sound.play()


root = ctk.CTk()
root.title('Имитация загрузки')
root.geometry("1000x700")
root.configure(fg_color='bisque')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Courier', size=25, weight='bold')
big_font = ctk.CTkFont(family='Courier', size=35, weight='bold')

sound = mixer.Sound('beep.mp3')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Загрузка', font=big_font)

frm = ctk.CTkFrame(master=root, width=500, height=100)
frm.configure(fg_color='bisque2', border_color='bisque4', border_width=3, corner_radius=20)
frm.grid_propagate(False)

lbl_frm = ctk.CTkLabel(master=frm)
lbl_frm.configure(text='Начните загрузку', font=my_font)

sl = ctk.CTkSlider(master=frm)
sl.configure(from_=0, to=100, width=400, fg_color='gray65', progress_color='gray35', button_color='black')
sl.set(0)

frm.rowconfigure(index=(0, 1), weight=1)
frm.columnconfigure(index=0, weight=1)
lbl_frm.grid(row=0, column=0, padx=10, pady=10)
sl.grid(row=1, column=0, padx=10, pady=10)

btn = ctk.CTkButton(master=root)
btn.configure(text="Загрузить", font=my_font, command=download, fg_color='bisque4')

lbl_start.grid(row=0, column=3, padx=10, pady=10)
frm.grid(row=1, column=3, padx=10, pady=10)
btn.grid(row=2, column=3, padx=20, pady=20, sticky="nsew")

root.mainloop()
