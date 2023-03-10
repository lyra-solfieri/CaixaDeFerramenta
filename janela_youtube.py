
import tkinter as tk
from tkinter import Label, StringVar, ttk, messagebox, filedialog
from datetime import date
import requests
from bs4 import BeautifulSoup
from config_youtube import YouTubeToMp3
import config_banco_de_dados

LARGEFONT = ("Verdana", 35)


class Tela_baixar_musicas(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

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
            directory_path = filedialog.askdirectory()
            label3 = ttk.Label(
                self, text=f'Diretório de Destino: {directory_path}')
            label3.grid(column=0, row=6)
            youtube_func = YouTubeToMp3(
                link=link, path=directory_path)
            youtube_func.baixando()
            youtube_func.converte()
            messagebox.showinfo(
                "Download", "Concluído e salvo em formato mp3 com sucesso")

            # Buttons
        self.botao_pesquisar = ttk.Button(
            self, text="Baixar", command=baixar)
        self.botao_pesquisar.grid(column=0, row=2, padx=10, pady=10)

        def salvar():
            link = self.texto_pesquisa.get()
            response = requests.get(link)
            content = response.content
            soup = BeautifulSoup(content, 'html.parser')
            # my_div = soup.find('div', {'id': 'title'})
            title = soup.find('title').text
            print(title)
            today = date.today()
            config_banco_de_dados.salvar_link(
                link=link, titulo=title, date=today)
            messagebox.showinfo(
                "Dados", "Salvo informações no banco")

        self.botao_baixar = ttk.Button(
            self, text="Salvar link", command=salvar)
        self.botao_baixar.grid(column=0, row=3, padx=10, pady=10)

        self.botao_back = ttk.Button(self, text="Links Baixados",
                                     command=lambda: controller.show_frame(Tela_musicas_salvas))
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

        tree = ttk.Treeview(self)
        cursor = config_banco_de_dados.get_dados()

        # Define the columns for the Treeview widget
        tree['columns'] = ('link', 'titulo', 'date')

        # Format the column headings
        tree.heading('#0', text='ID')
        tree.column('#0', width=50)
        tree.heading('link', text='Link')
        tree.column('link', width=300)
        tree.heading('titulo', text='Título')
        tree.column('titulo', width=300)
        tree.heading('date', text='Data')
        tree.column('date', width=100)

        # Insert the data into the Treeview widget
        for row in cursor.fetchall():
            tree.insert('', 'end', text=row[0],
                        values=(row[1], row[2], row[3]))

        tree.grid(row=1, column=0, sticky="nsew")

        def delete_button_click():
            # Get the ID of the selected row from the Treeview widget
            selected_item = tree.selection()[0]
            id = tree.item(selected_item)['text']

            # Call the delete_row function to delete the row from the table
            config_banco_de_dados.delete_row(id)

        # Buttons
        self.botao_back = ttk.Button(self, text="voltar",
                                     command=lambda: controller.show_frame(Tela_baixar_musicas))
        self.botao_back.grid(column=0, row=4, padx=10, pady=10)
