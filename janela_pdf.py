

from tkinter import Label, StringVar, ttk, messagebox, filedialog
import tkinter as tk
LARGEFONT = ("Verdana", 35)


class Tela_pdf_to_audio(tk.Frame):
    """_summary_

    Args:
        tk (_type_): _description_

    """

    def __init__(self, parent, controller):
        """_summary_

        Args:
            parent (_type_): _description_
            controller (_type_): _description_
        """
        tk.Frame.__init__(self, parent)

        # definindo o titulo da janela
        label = ttk.Label(
            self, text="Selecione o Pdf", font=LARGEFONT, justify="center")
        label.grid(row=0, column=0, padx=10, pady=10)

        # caixa de pesquisa

        # link = StringVar()
        # self.texto_pesquisa = ttk.Entry(self, width=40, textvariable=link)

        # self.texto_pesquisa.focus_set()
        # self.texto_pesquisa.grid(column=0, row=1)

        # arquivo
        def select_file():
            file_path = filedialog.askopenfilename()
            label2 = ttk.Label(self, text=f'Pdf selecionado: {file_path}')
            label2.grid(column=0, row=3)
            print(file_path)

        # botões
        self.botao_pesquisar = ttk.Button(
            self, text="selecionar arquivo pdf", command=select_file)
        self.botao_pesquisar.grid(column=0, row=2, padx=10, pady=10)
