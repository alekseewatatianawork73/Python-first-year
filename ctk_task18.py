import customtkinter as ctk
from pygame import mixer
mixer.init()


def volume(value):
    value = int(value)
    lbl_volume.configure(text=f'Громкость: {value}%')
    mixer.music.set_volume(value)


def toggle_music():
    if mixer.music.get_busy():
        mixer.music.stop()
        lbl_music.configure(text='Музыка выключена')
        btn.configure(text="Включить музыку")
    else:
        mixer.music.play(-1)
        lbl_music.configure(text='Музыка играет')
        btn.configure(text="Выключить музыку")


root = ctk.CTk()
root.title('Музыкальный плеер с регулировкой громкости')
root.geometry("1000x700")
root.configure(fg_color='thistle1')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Courier', size=30, weight='bold')

mixer.music.load("audio.mp3")
mixer.music.play(-1)

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text=f'Управление звуком', font=my_font)

frm = ctk.CTkFrame(master=root, width=500, height=300)
frm.configure(fg_color='thistle3', border_color='purple3', border_width=3, corner_radius=0)
frm.grid_propagate(False)

lbl_music = ctk.CTkLabel(master=frm)
lbl_music.configure(text=f'Музыка играет', font=my_font)

lbl_volume = ctk.CTkLabel(master=frm)
lbl_volume.configure(text=f'Громкость: 100%', font=my_font)

frm.rowconfigure(index=(0, 1), weight=1)
frm.columnconfigure(index=0, weight=1)
lbl_music.grid(row=0, column=0, padx=10, pady=10)
lbl_volume.grid(row=1, column=0, padx=10, pady=10)

btn = ctk.CTkButton(master=root)
btn.configure(text="Выключить музыку", font=my_font, command=toggle_music, fg_color='purple3')

lbl_sl = ctk.CTkLabel(master=root)
lbl_sl.configure(text=f'Громкость:', font=my_font)

sl = ctk.CTkSlider(master=root)
sl.configure(from_=0, to=100, fg_color='gray', progress_color='purple3', button_color='purple4', width=300, command=volume)
sl.set(100)

lbl_start.grid(row=0, column=3, padx=10, pady=10)
frm.grid(row=1, column=3, padx=10, pady=10)
btn.grid(row=2, column=3, padx=20, pady=20, sticky="ns")
lbl_sl.grid(row=3, column=3, padx=10, pady=10)
sl.grid(row=4, column=3, padx=10, pady=10)

root.mainloop()
