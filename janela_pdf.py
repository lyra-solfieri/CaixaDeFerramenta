

from tkinter import Label, StringVar, ttk, messagebox, filedialog
import tkinter as tk
from config_pdf import PdfToMp3
LARGEFONT = ("Verdana", 35)


class Tela_pdf_to_audio(tk.Frame):
    """_summary_

    Args:
        tk (_type_): _description_

    """

    def __init__(self, parent, controller):

        self.pdf_path = ''
        self.directory_path = ''
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

        # arquivo

        def select_file():
            self.pdf_path = filedialog.askopenfilename()
            label2 = ttk.Label(self, text=f'Pdf selecionado: {self.pdf_path}')
            label2.grid(column=0, row=3)
            print(self.pdf_path)

        self.botao_pesquisar = ttk.Button(
            self, text="selecionar arquivo pdf", command=select_file)
        self.botao_pesquisar.grid(column=0, row=2, padx=10, pady=10)

        # diretorio

        def select_directory():
            self.directory_path = filedialog.askdirectory()
            label3 = ttk.Label(
                self, text=f'Diretório de Destino: {self.directory_path}')
            label3.grid(column=0, row=5)
            print(self.directory_path)

        self.botao_pesquisar = ttk.Button(
            self, text="selecionar o destino do Mp3", command=select_directory)
        self.botao_pesquisar.grid(column=0, row=4, padx=10, pady=10)

        # salvar
        def converter():
            tomp3 = PdfToMp3(
                self.pdf_path, self.directory_path)
            tomp3.extrair_texto()

        self.botao_pesquisar = ttk.Button(
            self, text="Converter", command=converter)
        self.botao_pesquisar.grid(column=0, row=6, padx=10, pady=10)
