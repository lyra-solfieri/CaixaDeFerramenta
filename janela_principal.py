

from tkinter import ttk
import tkinter as tk
from janela_extrair_tabela_pdf import Tela_pdf_to_table
from janela_youtube import Tela_baixar_musicas, Tela_musicas_salvas
from janela_pdf import Tela_pdf_to_audio


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):
    """classe responsavel por criar os frame
        inicializa toda a aplicação

    Args:
        tk (_type_): tkinter
    """

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('550x450+500+500')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Tela_inicial, Tela_baixar_musicas, Tela_musicas_salvas, Tela_pdf_to_audio, Tela_pdf_to_table):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Tela_inicial)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Tela_inicial(tk.Frame):
    """Tela de inicialização do sistema
    com os dois botoes das funcionalidades 
    pincipais do sistema

    Args:
        tk (_type_): passando o tkinter como parametro
    """

    def __init__(self, parent, controller):
        """_summary_

        Args:
            parent (_type_): _description_
            controller (_type_): _description_
        """
        tk.Frame.__init__(self, parent)
        style = ttk.Style()

        style.configure("Custom.TButton", font=("Helvetica", 14), foreground="black", background="#007acc",
                        padding=10, borderwidth=0, width=20, height=3)
        style.configure("Custom.TLabel", foreground="#007acc",
                        background="#f0f0f0", font=("Courier", 22, "bold"))

        # usando o Label para exibir um texto
        self.texto_informativo = ttk.Label(
            self, text="Utilidades Python3", style="Custom.TLabel", justify="center")
        self.texto_informativo.grid(
            column=0, row=0, sticky="nsew", padx=10, pady=10)

        self.botao_procurar = ttk.Button(self, text="Baixar audio do youtube",
                                         command=lambda: controller.show_frame(Tela_baixar_musicas), style="Custom.TButton")
        self.botao_procurar.grid(column=0, row=1, padx=10, pady=10)

        self.botao_musicas_salvas = ttk.Button(self, text="Outra funcionalidade",
                                               command='lambda: controller.show_frame(Tela_musicas_salvas)', style="Custom.TButton")
        self.botao_musicas_salvas.grid(column=0, row=2, padx=10, pady=10)

        self.botao_pdf = ttk.Button(self, text="Pdf para Mp3",
                                               command=lambda: controller.show_frame(Tela_pdf_to_audio), style="Custom.TButton")
        self.botao_pdf.grid(column=0, row=3, padx=10, pady=10)

        self.tables_pdf = ttk.Button(
            self, text='Extrair Tabelas de Pdf', command=lambda: controller.show_frame(Tela_pdf_to_table), style="Custom.TButton")
        self.tables_pdf.grid(column=0, row=4, padx=10, pady=10)
