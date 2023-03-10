from tkinter import Label, StringVar, ttk, messagebox, filedialog
import tkinter as tk
from config_extract_tables_from_pdf import PDFTableExtractor
LARGEFONT = ("Verdana", 35)


class Tela_pdf_to_table(tk.Frame):

    def __init__(self, parent, controller):

        self.pdf_path = ''
        self.pages = ''

        tk.Frame.__init__(self, parent)
        style = ttk.Style()

        # Style Button
        style.configure("Custom.TButton", font=("Helvetica", 14), foreground="black", background="red",
                        padding=10, borderwidth=0, width=20, height=3)

        # definindo o titulo da janela
        label = ttk.Label(
            self, text="Selecione o Pdf para a extração das tabelas", font=LARGEFONT, justify="center")
        label.grid(row=0, column=0, padx=10, pady=10)

        def pdf_file(args):
            pass

        button_pdf = ttk.Button(
            self, text='Selecione o pdf', command='', style="Custom.TButton")
        button_pdf.grid(row=2, column=0, padx=10, pady=10)

        # caixa de pesquisa
        link = StringVar()
        self.texto_pesquisa = ttk.Entry(self, width=20, textvariable=link)
        self.texto_pesquisa.focus_set()
        self.texto_pesquisa.grid(column=0, row=4)

        label = ttk.Label(
            self, text="Número da página para extração da tabela Ex: 3-10 ou 3", font=('Verdana', 9), justify="center")
        label.grid(row=5, column=0, padx=15, pady=10)

        # List Box
        items = ["Csv", "Json", "Excel"]
        # create the Listbox widget
        listbox = tk.Listbox(self, height=3)
        # insert the items into the Listbox
        for item in items:
            listbox.insert(tk.END, item)
        listbox.grid(row=6, column=0)
