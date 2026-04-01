# Теория: метод after(), добавление звука в приложение
# Ссылка на файлы со звуками: https://drive.google.com/drive/folders/1URFPfih-PYEEh1sfTC3NKPZ6xdH6cdnt?usp=sharing
import customtkinter as ctk
from pygame import mixer  # используем модуль mixer из библиотеки pygame для подключения звука
mixer.init()  # при использовании pygame нужно обязательно инициализировать (подключать) нужные модули (здесь mixer)

# загрузка звукового файла (для фоновой музыки)
# его не нужно сохранять в отдельную переменную, и такой файл в программе должен быть единственным!
mixer.music.load('audio.mp3')

# загрузка короткого звукового файла (для нажатия на кнопку)
# его нужно сохранить в отдельную переменную, таких коротких звуков в программе может быть несколько
mus_btn = mixer.Sound('button_sound.mp3')


# функция для кнопки "Удалить текст на 3 секунды"
def press1():
    # при нажатии на кнопку один раз воспроизводится короткий звук
    mus_btn.play(0)
    # удаляем текстовую метку
    lbl.grid_forget()
    # ждём 3 секунды (3000 мс) и снова возвращаем текстовую метку на экран
    # используем lambda-функцию, потому что выполняется всего одно действие - размещение при помощи grid()
    root.after(3000, lambda: lbl.grid(row=1, column=3, padx=10, pady=10))
    # синтаксис: [окно, в котором выполняются действия].afler([время ожидания в мс],[функция, которую необходимо выполнить])
    # 1 секунда = 1000 миллисекунд


# функция для кнопки "Включить звук"
def press2():
    # при нажатии на кнопку один раз воспроизводится короткий звук
    mus_btn.play(0)
    # воспроизводим фоновую музыку без остановки
    mixer.music.play(-1)


# функция для кнопки "Выключить звук"
def press3():
    # при нажатии на кнопку один раз воспроизводится короткий звук
    mus_btn.play(0)
    # выключаем фоновую музыку
    mixer.music.stop()


# функция для кнопки "Мигающая надпись"
def press4():
    global cur_color, after_id
    # меняем цвет надписи
    if cur_color == 'black':
        cur_color = 'red'
    else:
        cur_color = 'black'
    lbl.configure(text_color=cur_color)
    # повторяем эту же функцию через полсекунды (500 миллисекунд)
    # сохраняем в переменную, чтобы позже можно было отменить мигание надписи
    after_id = root.after(500, press4)


# функция для кнопки "Немигающая надпись"
def press5():
    global after_id
    if after_id:
        root.after_cancel(after_id)  # отменяем повторяющиеся мигания


# функция для кнопки "Играет ли музыка?"
def press6():
    # проверяем, играет ли музыка, при помощи метода get_busy()
    if mixer.music.get_busy():
        lbl6.configure(text='Музыка играет')
    else:
        lbl6.configure(text='Музыка выключена')


# основная программа
root = ctk.CTk()
root.title("Моё приложение")
root.geometry("1000x500")

# сетка для размещения элементов в основновном окне (7 строк и 7 столбцов)
rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

my_font = ctk.CTkFont(family='Arial', size=20, weight='bold')
lbl_font = ctk.CTkFont(family='Arial', size=30, weight='bold')

# создаём надпись в окне
cur_color = 'black'  # текущий цвет текста
lbl = ctk.CTkLabel(master=root)
lbl.configure(text=f'Мой текст', text_color=cur_color, font=lbl_font)

# создаём кнопки
btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Удалить текст на 3 секунды", font=my_font, command=press1)

btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Включить звук", font=my_font, command=press2)

btn3 = ctk.CTkButton(master=root)
btn3.configure(text="Выключить звук", font=my_font, command=press3)

after_id = None  # переменная для выполнения мигания надписи
btn4 = ctk.CTkButton(master=root)
btn4.configure(text="Мигающая надпись", font=my_font, command=press4)

btn5 = ctk.CTkButton(master=root)
btn5.configure(text="Немигающая надпись", font=my_font, command=press5)

btn6 = ctk.CTkButton(master=root)
btn6.configure(text="Играет ли музыка?", font=my_font, command=press6)

lbl6 = ctk.CTkLabel(master=root)
lbl6.configure(text=f'...', font=my_font)

# размещение элементов в окне
lbl.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')
btn1.grid(row=2, column=3, padx=20, pady=20, sticky="nsew")
btn2.grid(row=3, column=2, padx=20, pady=20, sticky="nsew")
btn3.grid(row=3, column=4, padx=20, pady=20, sticky="nsew")
btn4.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")
btn5.grid(row=2, column=4, padx=20, pady=20, sticky="nsew")
btn6.grid(row=4, column=2, padx=20, pady=20, sticky="nsew")
lbl6.grid(row=4, column=4, padx=20, pady=20, sticky="nsew")

# бесконечный цикл для отображения окна приложения
root.mainloop()
