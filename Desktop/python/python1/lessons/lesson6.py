import tkinter as tk

window = tk.Tk()
window.title("الشهادة")  # Заголовок окна
window.geometry("900x700")
window.configure(bg="#0f172a")

# Объединяем две строки через перенос \n
label = tk.Label(
    window,
    text="أشهد أن لا إله إلا الله\nوأشهد أن محمداً رسول الله",
    font=("Arial", 48, "bold"),
    fg="white",
    bg="#0f172a",
    justify="center"
)

label.pack(expand=1)

window.mainloop()
