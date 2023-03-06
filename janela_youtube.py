
import tkinter as tk
from tkinter import Label, StringVar, ttk, messagebox
from datetime import date
from config_youtube import YouTubeToMp3
import config_banco_de_dados

LARGEFONT = ("Verdana", 35)


class Tela_baixar_musicas(tk.Frame):
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
        # self.title("Download")
        label = ttk.Label(
            self, text="Cole o link do youtube", font=LARGEFONT, justify="center")
        label.grid(row=0, column=0, padx=10, pady=10)

        # caixa de pesquisa
        link = StringVar()
        self.texto_pesquisa = ttk.Entry(self, width=40, textvariable=link)

        self.texto_pesquisa.focus_set()
        self.texto_pesquisa.grid(column=0, row=1)

        def baixar():
            link = self.texto_pesquisa.get()

            youtube_func = YouTubeToMp3(
                link=link, path='/home/bruno-lyra/Music/')
            youtube_func.baixando()
            youtube_func.converte()
            messagebox.showinfo(
                "Download", "Concluído e salvo em formato mp3 com sucesso")

            # Buttons
        self.botao_pesquisar = ttk.Button(
            self, text="Baixar", command=baixar)
        self.botao_pesquisar.grid(column=0, row=2, padx=10, pady=10)

        def salvar():
            # TODO: pegar o titulo com um web scraper
            link = self.texto_pesquisa.get()
            titulo = 'test'
            today = date.today()
            config_banco_de_dados.salvar_link(
                link=link, titulo=titulo, date=today)
            messagebox.showinfo(
                "Dados", "Salvo informações no banco")

        self.botao_baixar = ttk.Button(
            self, text="Salvar link", command=salvar)
        self.botao_baixar.grid(column=0, row=3, padx=10, pady=10)

        self.botao_back = ttk.Button(self, text="Voltar",
                                     command='')
        self.botao_back.grid(column=0, row=4, padx=10, pady=10)

        # TODO:Barra de progresso
        self.progressbar = ttk.Progressbar(self, mode='determinate')
        self.progressbar.grid(column=0, row=5)
        if (self.progressbar == True):
            self.i = Label(self, text="baixando...")
            self.i.grid(column=0, row=4)


class Tela_musicas_salvas(tk.Frame):
    """Todos os links salvos com o nome da musica
    referente ao link

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

        # Título
        label = ttk.Label(self, text="Todos os links salvos",
                          font=LARGEFONT, justify="center")
        label.grid(row=0, column=0, padx=10, pady=10)

        # TODO: adicionar tabelas com os links e o nome da música salva
        # config_banco_de_dados.links_salvos()

        # Buttons
        self.botao_back = ttk.Button(self, text="Come back",
                                     command='')
        self.botao_back.grid(column=0, row=4, padx=10, pady=10)
