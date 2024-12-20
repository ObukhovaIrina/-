import tkinter as tk
from tkinter import ttk, messagebox
import string

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

# Функция для взлома шифрованного сообщения
def brute_force_decrypt(text):
    results = []
    for shift in range(26):  # Перебираем все возможные сдвиги от 0 до 25
        decrypted_text = decrypt(text, shift)
        results.append(f"Сдвиг {shift}: {decrypted_text}")
    return "\n".join(results)

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
    brute_force_results = brute_force_decrypt(text)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, brute_force_results)


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