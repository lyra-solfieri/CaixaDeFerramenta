
import os
import pyttsx3
import PyPDF2


class PdfToMp3:
    """_summary_
    """

    def __init__(self, pdf: str, path: str):
        """_summary_

        Args:
            pdf (str): _description_
            path (str): _description_
        """
        self.pdf = pdf
        self.path = path

    def extrair_texto(self):
        with open(self.pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # variavel para armazenar o texto do pdf
            text = ''

            # loop em cada pagina do pdf
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            engine = pyttsx3.init()

            # Convert the text to speech
            engine.say(text)

            # Save the audio in MP3 format
            output_file = os.path.join(self.path, 'output.mp3')
            engine.save_to_file(text, output_file)

            # Run the pyttsx3 engine
            engine.runAndWait()


# output_dir = os.path.expanduser('~/output')
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# output_file = os.path.join(output_dir, 'output.mp3')
# engine.save_to_file(text, output_file)
