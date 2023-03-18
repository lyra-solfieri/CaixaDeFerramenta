from tkinter import Label, StringVar, ttk, messagebox, filedialog
import tkinter as tk
from config_extract_tables_from_pdf import PDFTableExtractor
from janela_principal import Tela_inicial
LARGEFONT = ("Verdana", 35)


class Tela_pdf_to_table(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller

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

        # selecionar pdf

        def select_file():
            self.pdf_path = filedialog.askopenfilename()
            label2 = ttk.Label(self, text=f'Pdf selecionado: {self.pdf_path}')
            label2.grid(column=0, row=3)
            print(self.pdf_path)

        button_pdf = ttk.Button(
            self, text='Selecione o pdf', command=select_file, style="Custom.TButton")
        button_pdf.grid(row=2, column=0, padx=10, pady=10)

        # caixa de pesquisa
        self.pages = StringVar()
        self.texto_pesquisa = ttk.Entry(
            self, width=20, textvariable=self.pages)
        self.texto_pesquisa.focus_set()
        self.texto_pesquisa.grid(column=0, row=4)

        label = ttk.Label(
            self, text="Número da página para extração da tabela Ex: 3-10 ou 3", font=('Verdana', 9), justify="center")
        label.grid(row=5, column=0, padx=15, pady=10)

        options = ["Csv", "Json", "Excel"]

        # create a Combobox widget
        self.drop_text = ttk.Combobox(self, values=options)
        self.drop_text.grid(row=6, column=0)

        def get_selected_value():
            # get the selected value
            selected_value = self.drop_text.get()
            print("Selected value:", selected_value)
            pdf_extractor = PDFTableExtractor(
                pdf_path=self.pdf_path, pages=self.pages.get())
            pdf_extractor.extract_table()
            if selected_value == 'Json':
                pdf_extractor.to_json('tabela.json')
            elif selected_value == 'Csv':
                pdf_extractor.to_csv('tabela.csv')
            elif selected_value == 'Excel':
                pdf_extractor.to_excel('tabela.excel')
            else:
                raise NameError('Nome incorreto')

        button_concluir = ttk.Button(
            self, text='Extrair', command=get_selected_value, style="Custom.TButton")
        button_concluir.grid(row=7, column=0, padx=10, pady=10)

        def return_to_main_menu():
            self.controller.show_frame(Tela_inicial)

        self.return_button = tk.Button(
            self, text='come back', command=return_to_main_menu)
        self.return_button.grid(column=0, row=8)
