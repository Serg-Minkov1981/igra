import pygame
import tkinter as tk
import random
import time
import subprocess
from tkinter import messagebox

# Список доступных цветов на русском языке и их соответствующие коды
colors = [
    ('Красный', 'red'),
    ('Зелёный', 'green'),
    ('Синий', 'blue'),
    ('Жёлтый', 'yellow'),
    ('Фиолетовый', 'purple'),
    ('Оранжевый', 'orange'),
    ('Коричневый', 'brown'),
    ('Серый', 'gray'),
    ('Бордовый', 'Maroon')
]

# Глобальные переменные для отслеживания игры
attempts = 0
correct_answers = 0
total_attempts = 0
start_time = None
time_limit = 0
buttons = []

# Функция для начала игры с указанным количеством попыток и временем
def start_game():
    global attempts, correct_answers, total_attempts, start_time, time_limit
    total_attempts = int(attempts_entry.get())
    time_limit = int(time_entry.get()) * 60 * 1000  # Перевод минут в миллисекунды
    attempts = 0
    correct_answers = 0
    start_time = int(time.time() * 1000)  # Время в миллисекундах
    attempts_label.config(text=f"Осталось попыток: {total_attempts - attempts}")
    result_label.config(text="")
    update_timer()
    pick_color()

# Функция для выбора случайного цвета и отображения его на экране с ложным названием
def pick_color():
    global current_color_name, current_color_code, false_color_name
    if attempts < total_attempts:
        current_color_name, current_color_code = random.choice(colors)
        false_color_name = random.choice([color[0] for color in colors if color[0] != current_color_name])
        color_label.config(text=false_color_name, bg=current_color_code)
        randomize_button_colors()
    else:
        end_game()

# Функция для случайного окрашивания кнопок
def randomize_button_colors():
    color_codes = [color[1] for color in colors]
    random.shuffle(color_codes)
    for i, button in enumerate(buttons):
        button.config(bg=color_codes[i], activebackground=color_codes[i])

# Функция для проверки ответа игрока
def check_answer(user_guess):
    global attempts, correct_answers
    if attempts < total_attempts:
        attempts += 1
        if user_guess == current_color_name:
            correct_answers += 1
        attempts_label.config(text=f"ЕЩЁ НЕМНОГО: {total_attempts - attempts}")
        pick_color()

def end_game():
    elapsed_time = int(time.time() * 1000) - start_time
    if correct_answers == total_attempts:
        display_fireworks()
    else:
        display_dislike()
        # Запуск скринсейвера при наличии ошибок
        subprocess.run(['python', 'C://Users//user//PycharmProjects//pythonProject2/telegram/matrix_screensaver.py'])  # Путь к файлу скринсейвера
    result_label.config(text=f"Игра окончена!\nПравильных ответов: {correct_answers} из {total_attempts}\nВремя выполнения: {elapsed_time / 1000:.2f} секунд", fg="blue")

# Функция для отображения анимации салюта
def display_fireworks():
    messagebox.showinfo("Результат", "Поздравляем! \n🎆 УРА 🎆" * 10)

# Функция для отображения дизлайка
def display_dislike():
    messagebox.showwarning("Результат", "👎 \n👎" * 10)

# Функция для обновления таймера
def update_timer():
    global start_time
    elapsed_time = int(time.time() * 1000) - start_time
    remaining_time = time_limit - elapsed_time
    if remaining_time <= 0 or attempts >= total_attempts:
        end_game()
    else:
        timer_label.config(text=f"ВРЕМЯ НЕ ВЕЧНО: {remaining_time} мс")
        root.after(1, update_timer)  # Обновляем каждые 100 мс

root = tk.Tk()
root.title("Угадай цвет")

attempts_label = tk.Label(root, text="Введите количество попыток:", font=('Arial', 16))
attempts_label.pack(pady=10)
attempts_entry = tk.Entry(root, font=('Arial', 16))
attempts_entry.pack(pady=10)

time_label = tk.Label(root, text="Введите время (минуты):", font=('Arial', 16))
time_label.pack(pady=10)
time_entry = tk.Entry(root, font=('Arial', 16))
time_entry.pack(pady=10)

start_button = tk.Button(root, text="ПОЕХАЛИ", command=start_game, font=('Arial', 16))
start_button.pack(pady=10)

color_label = tk.Label(root, text="Нажми 'ПОЕХАЛИ', чтобы начать", font=('Arial', 16), width=40, height=5)
color_label.pack(pady=20)

attempts_label = tk.Label(root, text="", font=('Arial', 16))
attempts_label.pack(pady=10)

timer_label = tk.Label(root, text="", font=('Arial', 16))
timer_label.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

for color_name, color_code in colors:
    button = tk.Button(buttons_frame, text=color_name, command=lambda c=color_name: check_answer(c), font=('Arial', 16), width=10)
    button.pack(side=tk.LEFT, padx=10, pady=10)
    buttons.append(button)

result_label = tk.Label(root, text="", font=('Arial', 16))
result_label.pack(pady=10)

root.mainloop()
