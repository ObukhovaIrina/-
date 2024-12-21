import tkinter as tk
from tkinter import ttk, messagebox
import string
#добавила новыую библиотеку
from collections import Counter


# Функция для генерации ключа шифрования
def generate_key(shift):
    return shift % 26


# Функция для шифрования текста
def encrypt(text, shift):
    key = generate_key(shift)
    result = ""
    for char in text:
        if char in string.ascii_letters:  # Проверяем, является ли символ буквой
            shifted = ord(char) + key
            if char.islower():  # Обработка строчных букв
                if shifted > ord('z'):
                    shifted -= 26
                result += chr(shifted)
            elif char.isupper():  # Обработка заглавных букв
                if shifted > ord('Z'):
                    shifted -= 26
                result += chr(shifted)
        else:
            result += char  # Если символ не буква, оставляем его без изменений
    return result


# Функция для дешифрования текста
def decrypt(text, shift):
    return encrypt(text, -shift)  # Используем шифрование с отрицательным сдвигом для дешифрования


# Функция для частотного анализа
def frequency_analysis(text):
    frequencies = Counter(text.lower())
    # Удаляем все символы, которые не являются буквами
    for char in string.ascii_lowercase:
        frequencies[char] = frequencies.get(char, 0)
    # Вычисляем наиболее встречающуюся букву
    return frequencies.most_common(1)[0][0]  # Возвращает наиболее частую букву


# Также добавила функция для взлома шифрованного сообщения с частотным анализом
def intelligent_decrypt(text, blocked_syllables):
    most_frequent_char = frequency_analysis(text)
    # Предполагаем, что наиболее часто встречающаяся буква шифра - это 'e' (это можно узнать в интернете)
    assumed_shift = (ord(most_frequent_char) - ord('e')) % 26

    decrypted_text = decrypt(text, assumed_shift)

    # Проверяем на наличие заблокированных слогов
    for syllable in blocked_syllables:
        if syllable in decrypted_text:
            return "Ошибка! Результат содержит заблокированные слоги."

    return decrypted_text


# Функции-обработчики для кнопок интерфейса
def on_encrypt():
    text = text_entry.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    encrypted_text = encrypt(text, shift)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, encrypted_text)


def on_decrypt():
    text = text_entry.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    decrypted_text = decrypt(text, shift)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, decrypted_text)


def on_brute_force():
    text = text_entry.get("1.0", tk.END).strip()
    blocked_syllables = ['аб', 'ав', 'ба', 'бо']  
    result_entry.delete("1.0", tk.END)

    decrypted_text = intelligent_decrypt(text, blocked_syllables)
    result_entry.insert(tk.END, decrypted_text)


root = tk.Tk()
root.title("Шифр Цезаря")

# Настройка стилей
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TText', font=('Helvetica', 12))

# Добавляем элементы интерфейса
ttk.Label(root, text="Введите текст:").pack(pady=5)
text_entry = tk.Text(root, height=5, width=50, font=('Helvetica', 12))
text_entry.pack(pady=5)

ttk.Label(root, text="Сдвиг (ключ):").pack(pady=5)
shift_entry = ttk.Entry(root, font=('Helvetica', 12))
shift_entry.pack(pady=5)

ttk.Button(root, text="Зашифровать", command=on_encrypt).pack(pady=5)
ttk.Button(root, text="Дешифровать", command=on_decrypt).pack(pady=5)
ttk.Button(root, text="Взломать", command=on_brute_force).pack(pady=5)

ttk.Label(root, text="Результат:").pack(pady=5)
result_entry = tk.Text(root, height=10, width=50, font=('Helvetica', 12))
result_entry.pack(pady=5)

# Запускаем главный цикл обработки событий
root.mainloop()
