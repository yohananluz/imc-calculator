"""Interface gráfica para a calculadora de IMC (usa tkinter, incluso no Python)."""

import tkinter as tk
from tkinter import messagebox, ttk

from imc import calcular_imc


def _parse_float(texto: str) -> float:
    texto = texto.strip().replace(",", ".")
    return float(texto)


def calcular():
    try:
        peso = _parse_float(entry_peso.get())
        altura = _parse_float(entry_altura.get())
    except ValueError:
        messagebox.showerror("Entrada inválida", "Use apenas números (vírgula ou ponto para decimais).")
        return

    if peso <= 0 or altura <= 0:
        messagebox.showwarning("Valores incorretos", "Peso e altura devem ser maiores que zero.")
        return

    imc, categoria = calcular_imc(peso, altura)
    lbl_imc.config(text=f"IMC: {imc:.2f}")
    lbl_classificacao.config(text=f"Classificação: {categoria}")


root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("340x220")
root.resizable(False, False)

frm = ttk.Frame(root, padding=16)
frm.grid(row=0, column=0, sticky="nsew")

ttk.Label(frm, text="Peso (kg):").grid(row=0, column=0, sticky="w", pady=(0, 4))
entry_peso = ttk.Entry(frm, width=20)
entry_peso.grid(row=1, column=0, sticky="ew", pady=(0, 10))

ttk.Label(frm, text="Altura (m):").grid(row=2, column=0, sticky="w", pady=(0, 4))
entry_altura = ttk.Entry(frm, width=20)
entry_altura.grid(row=3, column=0, sticky="ew", pady=(0, 10))

btn = ttk.Button(frm, text="Calcular", command=calcular)
btn.grid(row=4, column=0, pady=(0, 12))

lbl_imc = ttk.Label(frm, text="IMC: —")
lbl_imc.grid(row=5, column=0, sticky="w")
lbl_classificacao = ttk.Label(frm, text="Classificação: —")
lbl_classificacao.grid(row=6, column=0, sticky="w", pady=(4, 0))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frm.columnconfigure(0, weight=1)

if __name__ == "__main__":
    root.mainloop()
