import random
import tkinter as tk
from tkinter import ttk, messagebox

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Генерация ключа шифрования
def generate_key():
    length = random.randint(7, 15)  # Длина ключа от 7 до 15
    key = ''.join(random.choice(alphabet) for _ in range(length))
    return key


# Проверка, содержит ли строка русские буквы
def contains_russian(text):
    return any('\u0400' <= char <= '\u04FF' for char in text)


# Шифровка
def encrypt(input_text, key):
    if contains_russian(input_text):
        messagebox.showerror("Ошибка", "Введите текст на английском языке!")
        return ""

    input_text = input_text.upper()
    if not key:
        messagebox.showerror("Ошибка", "Введите или сгенерируйте ключ!")
        return ""

    return process_vigenere(input_text, key, True)


# Дешифровка
def decrypt(input_text, key):
    if contains_russian(input_text):
        messagebox.showerror("Ошибка", "Введите текст на английском языке!")
        return ""

    input_text = input_text.upper()
    if not key:
        messagebox.showerror("Ошибка", "Введите или сгенерируйте ключ!")
        return ""

    return process_vigenere(input_text, key, False)


# Процесс шифрования и дешифрования Виженера
def process_vigenere(text, key, is_encrypt):
    result = ''
    key_index = 0

    for char in text:
        text_index = alphabet.find(char)

        if text_index == -1:
            result += char  # Не изменяем символы, не входящие в алфавит
            continue

        key_index_value = alphabet.find(key[key_index % len(key)])  # Получаем индекс символа ключа
        if is_encrypt:
            new_index = (text_index + key_index_value) % len(alphabet)  # Шифрование
        else:
            new_index = (text_index - key_index_value + len(alphabet)) % len(alphabet)  # Дешифрование

        result += alphabet[new_index]
        key_index += 1

    return result


# Обработка шифрования
def on_encrypt():
    input_text = text_entry.get("1.0", tk.END).strip()
    key = shift_entry.get().strip()

    encrypted_text = encrypt(input_text, key)
    if encrypted_text:
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, encrypted_text)


# Обработка дешифрования
def on_decrypt():
    input_text = text_entry.get("1.0", tk.END).strip()
    key = shift_entry.get().strip()

    decrypted_text = decrypt(input_text, key)
    if decrypted_text:
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, decrypted_text)


# Обработка генерации ключа
def on_generate_key():
    key = generate_key()
    shift_entry.delete(0, tk.END)
    shift_entry.insert(0, key)


# Создание основного окна
root = tk.Tk()
root.title("Шифр Виженера")

# Настройка стиля
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TText', font=('Helvetica', 12))

# Добавляем элементы интерфейса
ttk.Label(root, text="Введите текст:").pack(pady=5)
text_entry = tk.Text(root, height=5, width=50, font=('Helvetica', 12))
text_entry.pack(pady=5)

ttk.Label(root, text="Введите или сгенерируйте ключ:").pack(pady=5)
shift_entry = ttk.Entry(root, font=('Helvetica', 12))
shift_entry.pack(pady=5)

# Кнопки шифрования и дешифрования
ttk.Button(root, text="Сгенерировать ключ", command=on_generate_key).pack(pady=5)
ttk.Button(root, text="Зашифровать", command=on_encrypt).pack(pady=5)
ttk.Button(root, text="Дешифровать", command=on_decrypt).pack(pady=5)

# Результат
ttk.Label(root, text="Результат:").pack(pady=5)
result_textbox = tk.Text(root, height=10, width=50, font=('Helvetica', 12))
result_textbox.pack(pady=5)

# Запуск главного цикла
root.mainloop()
