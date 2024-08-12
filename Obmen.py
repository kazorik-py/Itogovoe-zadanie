from tkinter import *
from tkinter import  ttk
from tkinter import messagebox as mb
import requests
import json

def update_currency_label(event):
    # Получаем полное название валюты из словаря и обновляем метку
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)

def exchange():
    t_code = target_combobox.get()
    base_code=base_combobox.get()
    if t_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()

            data = response.json()

            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                base=currencies[base_code]
                target=currencies[t_code]
                #currency_name=currencies[code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {target} за 1{base}")
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите код валюты")
currencies = {
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум",
    "USD": "Американский доллар"}

window = Tk()
window.title("Курс обмена валюты к доллару")
window.geometry("360x300")

Label(text="Базовая валюта:").pack(padx=10, pady=10)
base_combobox=ttk.Combobox(values=list (currencies.keys()))
base_combobox.pack(padx=10, pady=10)
#b_combobox.bind("<<ComboboxSelected>>", update_currency_label)


Label(text="Целевая валюта:").pack(padx=10, pady=10)

target_combobox=ttk.Combobox(values=list (currencies.keys()))
target_combobox.pack(padx=10, pady=10)
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)


Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()

