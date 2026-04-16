# Тема: холст Canvas — рисование в customtkinter
# ссылка на картинку пчелы: https://drive.google.com/file/d/1qNlq8z4rkSAhWQH53okyFIewLARr2xI1/view?usp=sharing
import customtkinter as ctk
from PIL import Image, ImageTk


def clear_canvas():
    # удаляем все объекты с холста
    pict.delete('all')


def del_image():
    # удаляем с холста картинку bee_image
    pict.delete(bee_image)


def del_rect():
    # удаляем с холста прямоугольник rect
    pict.delete(rect)


def move_triag():
    # двигаем треугольник triangle вправо на 50 пикселей и вниз на 20 пикселей
    pict.move(triangle, 50, 20)
    # двигаем стрелку line2 влево на 20 пикселей и вверх на 40 пикселей
    pict.move(line2, -20, -40)


def fill_triag():
    # меняем свойство fill (заливка) треугольника при помощи метода itemconfig
    pict.itemconfig(triangle, fill='red')


# основная программа
root = ctk.CTk()
root.title("Холст для рисования")
root.geometry("1200x900")

rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Courier', size=25, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Рисуем на холсте Canvas', font=my_font)

# создаём холст pict при помощи класса CTkCanvas()
pict = ctk.CTkCanvas(master=root)
pict.configure(width='500', height='500', bg='lightyellow', cursor='hand2', relief='groove', borderwidth=5)
# cursors: cross, arrow, hand2, wait
# relief: flat, groove, raised, ridge, solid, или sunken

# пишем синюю надпись на холсте (центр надписи в точке с координатами x = 125, y = 20)
# при наведении курсора надпись становится красной
my_text = pict.create_text(125, 20, text='Моя надпись', justify='center', font=my_font, fill='blue', activefill='red')

# рисуем красную линию от точки с координатами (10, 10) до точки с координатами (230, 230), толщина линии 5 пикселей
line1 = pict.create_line(10, 10, 230, 230, fill='red', width=5)

# рисуем синюю пунктирную (dash) линию со стрелкой на конце от точки (100, 240) до точки (100, 100)
# толщиной 5 пикселей, при наведении курсора линия становится зелёной
line2 = pict.create_line(100, 240, 100, 100, fill='blue', width=5, arrow='last', dash=(50, 2),
                 activefill='green', arrowshape=(10, 20, 10))
# arrow: first, last или both

# рисуем прямоугольник (левый верхний угол в точке (250, 20), правый нижний в точке (350, 100)
rect = pict.create_rectangle(250, 20, 350, 100, fill='red', outline='blue', width=3, activeoutline='green',
                      activedash=(5, 4), activefill='yellow')

# рисуем треугольник с вершинами в точках (400, 20), (450, 120), (350, 120)
triangle = pict.create_polygon(400, 20, 450, 120, 350, 120)

# рисуем прямоугольник и овал внутри этого прямоугольника
rect_oval = pict.create_rectangle(20, 250, 180, 350, width=5)
my_oval = pict.create_oval(20, 250, 180, 350, fill='white', outline='red', width=2)

# рисуем прямоугольник
rect_arc = pict.create_rectangle(200, 300, 450, 450, width=5)
# рисуем внутри этого прямоугольника красный сектор от 0 градусов (длина дуги - 90 градусов)
red_pie = pict.create_arc(200, 300, 450, 450, start=0, extent=90, fill='red')
# рисуем оранжевый сектор от 180 градусов (длина дуги - 25 градусов)
orange_pie = pict.create_arc(200, 300, 450, 450, start=180, extent=25, fill='orange')
# рисуем хорду (сегмент) зеленого цвета от 260 градусов (длина - 100 градусов)
green_chord = pict.create_arc(200, 300, 450, 450, start=260, extent=100, style='chord', fill='green')
# рисуем дугу синего цвета от 160 градусов (длина - 70 градусов)
blue_arc = pict.create_arc(200, 300, 450, 450, start=100, extent=70, style='arc', outline='blue', width=5)
#style: pieslice - сектор, chord - хорда, arc - дуга

# добавляем на холст картинку bee.png
my_image = Image.open("bee.png")  # загружаем картинку
my_object = ImageTk.PhotoImage(my_image)  # делаем картинку объектом (чтобы ее можно было разместить)
# размещаем центр картинки в координатах (350, 200)
bee_image = pict.create_image(350, 200, anchor='center', image=my_object)

# создаём кнопку и текстовую надпись
button = ctk.CTkButton(master=pict, text="Нажми меня", font=my_font)
label = ctk.CTkLabel(master=pict, text="Я на Canvas", font=my_font)
# размещаем их на холсте
my_btn = pict.create_window(100, 410, window=button, anchor='center')
my_lbl = pict.create_window(100, 460, window=label, anchor='center')

# кнопки для изменения объектов на холсте
btn_clear = ctk.CTkButton(master=root)
btn_clear.configure(text="Очистить холст", font=my_font, command=clear_canvas)

btn_del1 = ctk.CTkButton(master=root)
btn_del1.configure(text="Удалить картинку", font=my_font, command=del_image)

btn_del2 = ctk.CTkButton(master=root)
btn_del2.configure(text="Удалить прямоугольник", font=my_font, command=del_rect)

btn_move = ctk.CTkButton(master=root)
btn_move.configure(text="Подвинуть треугольник и стрелку", font=my_font, command=move_triag)

btn_fill = ctk.CTkButton(master=root)
btn_fill.configure(text="Покрасить треугольник", font=my_font, command=fill_triag)

# размещение элементов в главном окне root
lbl_start.grid(row=0, column=3, padx=5, pady=5)
pict.grid(row=1, column=3, padx=5, pady=5)
btn_clear.grid(row=2, column=3, padx=5, pady=5)
btn_del1.grid(row=3, column=2, padx=5, pady=5)
btn_del2.grid(row=3, column=4, padx=5, pady=5)
btn_move.grid(row=4, column=3, padx=5, pady=5)
btn_fill.grid(row=5, column=3, padx=5, pady=5)

root.mainloop()
