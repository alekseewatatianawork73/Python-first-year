import customtkinter as ctk
from pygame import mixer
mixer.init()

seconds = 0
timer = False


def start_timer():
    global seconds, timer
    if not timer:
        seconds = int(entr.get())
        timer = True
    if seconds >= 0:
        lbl_res.configure(text=f'{seconds} сек.')
        seconds -= 1
        root.after(1000, start_timer)
    else:
        lbl_res.configure(text=f'Время вышло!')
        sound.play(3)
        timer = False


root = ctk.CTk()
root.title('Таймер с сигналом')
root.geometry("1000x700")
root.configure(fg_color='lightcyan')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Courier', size=25, weight='bold')

sound = mixer.Sound('beep.mp3')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Таймер', font=my_font)

entr = ctk.CTkEntry(master=root)
entr.configure(font=my_font, justify='center', placeholder_text='время в секундах')

frm = ctk.CTkFrame(master=root, width=500, height=300)
frm.configure(fg_color='lightblue2', border_color='lightblue4', border_width=3, corner_radius=0)
frm.grid_propagate(False)

lbl_time = ctk.CTkLabel(master=frm)
lbl_time.configure(text='Осталось времени:', font=my_font)

lbl_res = ctk.CTkLabel(master=frm)
lbl_res.configure(text='0 сек.', font=my_font)

frm.rowconfigure(index=(0, 1), weight=1)
frm.columnconfigure(index=0, weight=1)
lbl_time.grid(row=0, column=0, padx=10, pady=10)
lbl_res.grid(row=1, column=0, padx=10, pady=10)

btn = ctk.CTkButton(master=root)
btn.configure(text="Запустить таймер", font=my_font, command=start_timer, fg_color='lightblue4')

lbl_start.grid(row=0, column=3, padx=10, pady=10)
entr.grid(row=1, column=3, padx=10, pady=10, sticky="ew")
frm.grid(row=2, column=3, padx=10, pady=10)
btn.grid(row=3, column=3, padx=20, pady=20, sticky="ns")

root.mainloop()
