
from tkinter import ttk
import tkinter as tk


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window_width = 600
        window_height = 500

        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = (screen_width/2) - (window_width/2)
        y = (screen_height/2) - (window_height/2)

        # Set the position and size of the window
        self.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

        self.title('Caixa de Ferramenta')

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Frames/Telas
        from janela_extrair_tabela_pdf import Tela_pdf_to_table
        from janela_youtube import Tela_baixar_musicas, Tela_musicas_salvas
        from janela_pdf import Tela_pdf_to_audio

        self.frames = {}
        for F in (Tela_inicial, Tela_baixar_musicas, Tela_musicas_salvas, Tela_pdf_to_audio, Tela_pdf_to_table):

            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Tela_inicial)

    def show_frame(self, cont):
        if cont not in self.frames:
            self.frames[cont] = Tela_inicial(self, self.container)
            self.frames[cont].pack(side="top", fill="both", expand=True)

        frame = self.frames[cont]
        frame.tkraise()


class Tela_inicial(tk.Frame):
    """Tela de inicialização do sistema
    com os dois botoes das funcionalidades 
    pincipais do sistema

    """

    def __init__(self, parent, controller):
        from janela_extrair_tabela_pdf import Tela_pdf_to_table
        from janela_youtube import Tela_baixar_musicas
        from janela_pdf import Tela_pdf_to_audio

        tk.Frame.__init__(self, parent)
        self.controller = controller
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
        self.botao_procurar.grid(
            column=0, row=1, padx=10, sticky="nsew", pady=10)

        self.botao_musicas_salvas = ttk.Button(self, text="Outra funcionalidade",
                                               command='lambda: controller.show_frame(Tela_musicas_salvas)', style="Custom.TButton")
        self.botao_musicas_salvas.grid(
            column=0, row=2, padx=10, pady=10, sticky='nsew')

        self.botao_pdf = ttk.Button(self, text="Pdf para Mp3",
                                               command=lambda: controller.show_frame(Tela_pdf_to_audio), style="Custom.TButton")
        self.botao_pdf.grid(column=0, row=3, padx=10, pady=10, sticky='nsew')

        self.tables_pdf = ttk.Button(
            self, text='Extrair Tabelas de Pdf', command=lambda: controller.show_frame(Tela_pdf_to_table), style="Custom.TButton")
        self.tables_pdf.grid(column=0, row=4, padx=10, pady=10, sticky='nsew')

        # Center the label and buttons in the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.texto_informativo.grid_configure(sticky="nsew")
        self.botao_procurar.grid_configure(sticky="nsew")
        self.botao_musicas_salvas.grid_configure(sticky="nsew")
        self.botao_pdf.grid_configure(sticky="nsew")
        self.tables_pdf.grid_configure(sticky="nsew")
