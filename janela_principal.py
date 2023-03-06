

from tkinter import ttk
import tkinter as tk
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

        for F in (Tela_inicial, Tela_baixar_musicas, Tela_musicas_salvas, Tela_pdf_to_audio):

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

        # usando o Label para exibir um texto
        self.texto_informativo = ttk.Label(self,
                                           text="Utilidades Python3",
                                           font=("Courier 22 bold"), justify="center")
        self.texto_informativo.grid(column=0, row=0)

        self.botao_procurar = ttk.Button(self, text="Procurar Músicas",
                                         command=lambda: controller.show_frame(Tela_baixar_musicas))
        self.botao_procurar.grid(column=0, row=1, padx=10, pady=10)

        self.botao_musicas_salvas = ttk.Button(self, text="Links Salvos",
                                               command=lambda: controller.show_frame(Tela_musicas_salvas))
        self.botao_musicas_salvas.grid(column=0, row=2, padx=10, pady=10)

        self.botao_musicas_salvas = ttk.Button(self, text="Pdf para Mp3",
                                               command=lambda: controller.show_frame(Tela_pdf_to_audio))
        self.botao_musicas_salvas.grid(column=0, row=3, padx=10, pady=10)
