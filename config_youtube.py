from pytube import YouTube
import moviepy.editor as mp
import re
import os


class YouTubeToMp3():

    """Usuando  as bibliotecas:
        pytube: Usada para baixar o video do youtube em formato mp4
        moviepy: Usada para converter para mp3 e para salvar no local destino

    """

    def __init__(self, link: str, path: str):
        """

        Args:
            link (str): url do video ex:https://www.youtube.com/watch?v=Id_JOzSgOu4 
            path (str): local onde será armazenado o arquivo
        """
        self.link = link
        self.path = path

    def baixando(self):
        youtube = YouTube(self.link)
        youtube_stream = youtube.streams.filter(
            only_audio=True).first()
        youtube_stream.download(self.path)

    def converte(self):
        for file in os.listdir(self.path):
            if re.search('mp4', file):
                mp4_path = os.path.join(self.path, file)
                mp3_path = os.path.join(
                    self.path, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)

    def titulo_musica(self):
        pass
