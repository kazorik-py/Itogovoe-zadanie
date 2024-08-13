from tkinter import *
from tkinter import messagebox as mb
import requests
import json

def exchange():
    code = entry.get().lower()  # Приводим введенный код к нижнему регистру
    if code:
        try:
            response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
            response.raise_for_status()
            data = response.json()

            if code in data['rates']:
                exchange_rate = data['rates'][code]['value']
                mb.showinfo("Курс обмена", f"Курс {code.upper()}: {exchange_rate}")
            else:
                mb.showwarning("Внимание", "Код криптовалюты не найден")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Введите код криптовалюты")

window = Tk()
window.title("Курс криптовалют")
window.geometry("400x200")

Label(text="Выберите код криптовалюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к БИТКОИНУ", command=exchange).pack(padx=10, pady=10)

window.mainloop()
