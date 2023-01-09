from datetime import date
from config_youtube import YouTubeToMp3
import config_banco_de_dados
import tkinter as tk
from tkinter import Label, StringVar, ttk, messagebox
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

        for F in (Tela_inicial, Tela_baixar_musicas, Tela_musicas_salvas):

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
        # definindo o titulo da janela
        # self.title("mp3 load")

        # usando o Label para exibir um texto
        self.texto_informativo = ttk.Label(self,
                                           text="Baixe suas musicas favoritas",
                                           font=("Courier 22 bold"), justify="center")
        self.texto_informativo.grid(column=0, row=0)

        self.botao_procurar = ttk.Button(self, text="Procurar Músicas",
                                         command=lambda: controller.show_frame(Tela_baixar_musicas))
        self.botao_procurar.grid(column=0, row=1, padx=10, pady=10)

        self.botao_musicas_salvas = ttk.Button(self, text="Links Salvos",
                                               command=lambda: controller.show_frame(Tela_musicas_salvas))
        self.botao_musicas_salvas.grid(column=0, row=2, padx=10, pady=10)


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
                                     command=lambda: controller.show_frame(Tela_inicial))
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
                                     command=lambda: controller.show_frame(Tela_inicial))
        self.botao_back.grid(column=0, row=4, padx=10, pady=10)
