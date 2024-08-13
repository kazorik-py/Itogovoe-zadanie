from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import json

def update_currency_label(event):
    code=combobox.get()
    name=currencies[code]
    currency_label.config(text=name)
def exchange():
    code =combobox.get()#.lower()  # Приводим введенный код к нижнему регистру
    if code:
        try:
            response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
            response.raise_for_status()
            data = response.json()

            if code in data['rates']:
                exchange_rate = data['rates'][code]['value']
                currency_name=currencies[code]
                mb.showinfo("Курс обмена", f"Курс{currency_name} {code.upper()}: {exchange_rate}")
            else:
                mb.showwarning("Внимание", "Код криптовалюты не найден")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Введите код криптовалюты")

currencies={
    "BTC":"Bitkoin",
    "ETH":"Ether",
    "LTC":"Litecoin",
    "BCH":"Bitcoin Cash",
    "BNB":"Binance Coin"
}

window = Tk()
window.title("Курс криптовалют")
window.geometry("400x200")

Label(text="Выберите код валюты").pack(padx=10, pady=10)

combobox= ttk.Combobox(values=list(currencies.keys()))
combobox.pack(padx=10,pady=10)
combobox.bind("<<ComboboxSelected>>",update_currency_label)

currency_label = ttk.Label



Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()