# ссылка на картинку домика: https://drive.google.com/file/d/1iwHUmbT6gg0uN74NGVV8B8GMRbGbiNKl/view?usp=sharing
import customtkinter as ctk
from PIL import Image, ImageTk


def clear_canvas():
    pict.delete('all')


def show_house():
    pict.delete('all')
    if cmb.get() == 'картинка':
        pict.create_image(250, 200, anchor='center', image=house)
    else:
        pict.create_rectangle(290, 40, 310, 100, fill='gray')
        pict.create_polygon(250, 20, 350, 120, 150, 120, fill='burlywood4')
        pict.create_rectangle(150, 120, 350, 300, fill='burlywood3')
        pict.create_rectangle(230, 180, 270, 230, fill='yellow')
        pict.create_line(0, 300, 500, 300, width=5, fill='forestgreen')


root = ctk.CTk()
root.title("Холст для рисования")
root.geometry("1000x700")
root.configure(fg_color='lightgreen')

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Courier', size=25, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Домик на холсте', font=my_font)

pict = ctk.CTkCanvas(master=root)
pict.configure(width='500', height='400', bg='lightyellow', cursor='hand2', relief='sunken', borderwidth=5)

cmb = ctk.CTkComboBox(master=root)
cmb.configure(justify='center', font=my_font, values=['рисунок', 'картинка'])
cmb.set('рисунок')

image = Image.open('house.png')
house = ImageTk.PhotoImage(image)

btn_clear = ctk.CTkButton(master=root)
btn_clear.configure(text="Спрятать домик", font=my_font, command=clear_canvas, fg_color='forestgreen')

btn_show = ctk.CTkButton(master=root)
btn_show.configure(text="Показать домик", font=my_font, command=show_house, fg_color='forestgreen')

lbl_start.grid(row=0, column=3, padx=5, pady=5)
pict.grid(row=2, column=3, padx=5, pady=5)
cmb.grid(row=1, column=3, padx=5, pady=5)
btn_clear.grid(row=4, column=3, padx=5, pady=5)
btn_show.grid(row=3, column=3, padx=5, pady=5)

root.mainloop()
