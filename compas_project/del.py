import tkinter as tk

def on_key_press(event, pan):
    # Получаем текущее содержимое поля ввода
    current_text = pan.get()

    # Если пользователь пытается удалить текст (нажимаем Backspace или Delete)
    if event.keysym in ('BackSpace', 'Delete'):
        # Проверяем, если текущий текст равен исходному, отменяем действие
        if current_text == "Привет, мир!":
            return "break"

# Создаем основное окно
root = tk.Tk()
root.minsize(400,400)
root.title("Поле ввода с защищенным текстом")

# Создаем поле ввода
pan = tk.Entry(root)
pan.pack(pady=10)  # Добавляем отступ по вертикали

# Устанавливаем начальный текст в поле ввода
pan.insert(0, "Привет, мир!")  # Вставляем текст

# Привязываем обработчик событий к полю ввода
pan.bind("<KeyPress>", on_key_press*(pan))

# Запускаем главный цикл приложения
root.mainloop()
