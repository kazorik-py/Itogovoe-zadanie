from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json

def exchange():
    code = combobox.get()
    if code:
        try:
            response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
            response.raise_for_status()
            data = response.json()

            if code in data['rates']:
                exchange_rates = data['rates'][code]['value']
                mb.showinfo("Курс обмена", f"Курс {exchange_rates}: {code} за 1 биткоин???")
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

cur = ['rub','eur','usd','jpy','clp','dkk','cny','aed']
combobox = ttk.Combobox(values=cur)
combobox.pack(padx=10, pady=10)


Button(text="Получить курс обмена к БИТКОИНУ", command=exchange).pack(padx=10, pady=10)

window.mainloop()
