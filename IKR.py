from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json


def update_c_label(event):
    code = combobox.get()
    #name = cur(code)   На что он ругается?
    c_label.config(text=name)


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


cur = {
    'rub':'Российский рубль',
    'eur':'Евро',
    'usd':'Американский доллар',
    'jpy':'Японская йена',
    'clp':'Чилийский пессо',
    'dkk':'Датская крона',
    'cny':'Китайский юань',
    'aed':'Дирхам ОАЭ'}

window = Tk()
window.title("Курс криптовалют")
window.geometry("400x200")

Label(text="Выберите код криптовалюты").pack(padx=10, pady=10)


combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10,pady=10)

Button(text="Получить курс обмена к БИТКОИНУ", command=exchange).pack(padx=10, pady=10)

window.mainloop()
