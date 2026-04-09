import customtkinter as ctk

my_text = None


def txt_save():
    global my_text
    my_text = txt_input.get('0.0', 'end')
    lbl_space.configure(text='Количество символов (с пробелами):')
    lbl_count.configure(text='Количество символов (без пробелов):')
    lbl_words.configure(text='Количество слов:')
    entr.delete(0, 'end')
    lbl_res.configure(text='...')


def txt_review():
    global my_text
    with_space = len(my_text)
    lbl_space.configure(text=f'Количество символов (с пробелами): {with_space}')

    my_text_2 = my_text.replace(' ', '')
    without_space = len(my_text_2)
    lbl_count.configure(text=f'Количество символов (без пробелов): {without_space}')

    words = my_text.split()
    count_words = len(words)
    lbl_words.configure(text=f'Количество слов: {count_words}')


def find_word():
    global my_text
    my_word = entr.get()
    count = my_text.count(my_word)
    lbl_res.configure(text=f'Слово встречается в тексте {count} раз(а).')


# основная программа
ctk.set_appearance_mode('dark')
root = ctk.CTk()
root.title('Работа с текстом')
root.geometry("1000x700")

# сетка для размещения элементов в главном окне root
rows, columns = 7, 7
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

# шрифты
mini_font = ctk.CTkFont(family='Courier', size=20, weight='bold')
my_font = ctk.CTkFont(family='Courier', size=25, weight='bold')
big_font = ctk.CTkFont(family='Courier', size=30, weight='bold')

lbl_start = ctk.CTkLabel(master=root)
lbl_start.configure(text='Анализ текста', font=big_font)

tbw = ctk.CTkTabview(master=root)
tbw.configure(width=900, height=500)
tbw._segmented_button.configure(font=mini_font)
tbw.grid_propagate(False)

tbw.add('Ввод текста')
tbw.add('Анализ текста')
tbw.add('Дополнительно')

input_tbw = tbw.tab('Ввод текста')

lbl_input = ctk.CTkLabel(master=input_tbw)
lbl_input.configure(text='Введите ваш текст:', font=my_font)

txt_input = ctk.CTkTextbox(master=input_tbw)
txt_input.configure(font=my_font, wrap='word', width=500, height=200, border_width=3)

btn_save = ctk.CTkButton(master=input_tbw)
btn_save.configure(text="Сохранить", font=my_font, command=txt_save)

input_tbw.rowconfigure(index=(0, 1, 2), weight=1)
input_tbw.columnconfigure(index=0, weight=1)
lbl_input.grid(row=0, column=0, padx=10, pady=10)
txt_input.grid(row=1, column=0, padx=10, pady=10)
btn_save.grid(row=2, column=0, padx=10, pady=10)

review_tbw = tbw.tab('Анализ текста')

lbl_space = ctk.CTkLabel(master=review_tbw)
lbl_space.configure(text='Количество символов (с пробелами):', font=my_font)

lbl_count = ctk.CTkLabel(master=review_tbw)
lbl_count.configure(text='Количество символов (без пробелов):', font=my_font)

lbl_words = ctk.CTkLabel(master=review_tbw)
lbl_words.configure(text='Количество слов:', font=my_font)

btn_review = ctk.CTkButton(master=review_tbw)
btn_review.configure(text="Рассчитать", font=my_font, command=txt_review)

review_tbw.rowconfigure(index=(0, 1, 2, 3), weight=1)
review_tbw.columnconfigure(index=0, weight=1)
lbl_space.grid(row=0, column=0, padx=10, pady=10)
lbl_count.grid(row=1, column=0, padx=10, pady=10)
lbl_words.grid(row=2, column=0, padx=10, pady=10)
btn_review.grid(row=3, column=0, padx=10, pady=10)

add_tbw = tbw.tab('Дополнительно')

lbl_add = ctk.CTkLabel(master=add_tbw)
lbl_add.configure(text='Поиск слов', font=big_font)

lbl_find = ctk.CTkLabel(master=add_tbw)
lbl_find.configure(text='Введите искомое слово:', font=my_font)

entr = ctk.CTkEntry(master=add_tbw)
entr.configure(justify='center', font=my_font)

btn_find = ctk.CTkButton(master=add_tbw)
btn_find.configure(text="Найти", font=my_font, command=find_word)

lbl_res = ctk.CTkLabel(master=add_tbw)
lbl_res.configure(text='...', font=my_font)

add_tbw.rowconfigure(index=(0, 1, 2, 3, 4), weight=1)
add_tbw.columnconfigure(index=0, weight=1)
lbl_add.grid(row=0, column=0, padx=10, pady=10)
lbl_find.grid(row=1, column=0, padx=10, pady=10)
entr.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
btn_find.grid(row=3, column=0, padx=10, pady=10)
lbl_res.grid(row=4, column=0, padx=10, pady=10)

# размещение элементов в главном окне root
lbl_start.grid(row=0, column=3, padx=10, pady=10)
tbw.grid(row=1, column=3, padx=10, pady=10)

root.mainloop()
