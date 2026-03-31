# Теория: метод after(), добавление звука в приложение
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
    lbl1.grid_forget()
    # ждём 3 секунды (3000 мс) и снова возвращаем текстовую метку на экран
    # используем lambda-функцию, потому что выполняется всего одно действие - размещение при помощи grid()
    root.after(3000, lambda: lbl1.grid(row=1, column=3, padx=10, pady=10))
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

my_font = ctk.CTkFont(family='Arial', size=25, weight='bold')

# создаём виджеты
lbl1 = ctk.CTkLabel(master=root)
lbl1.configure(text=f'Text', font=my_font)
lbl1.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')

btn1 = ctk.CTkButton(master=root)
btn1.configure(text="Удалить текст на 3 секунды", font=my_font, command=press1)
btn1.grid(row=4, column=3, padx=20, pady=20, sticky="nsew")

btn2 = ctk.CTkButton(master=root)
btn2.configure(text="Включить звук", font=my_font, command=press2)
btn2.grid(row=5, column=2, padx=20, pady=20, sticky="nsew")

btn3 = ctk.CTkButton(master=root)
btn3.configure(text="Выключить звук", font=my_font, command=press3)
btn3.grid(row=5, column=4, padx=20, pady=20, sticky="nsew")

# бесконечный цикл для отображения окна приложения
root.mainloop()
