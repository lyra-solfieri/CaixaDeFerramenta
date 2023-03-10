import camelot
import pandas as pd
import json


class PDFTableExtractor:
    def __init__(self, pdf_path, pages):
        self.pdf_path = pdf_path
        self.pages = pages

    def extract_table(self):
        tables = camelot.read_pdf(self.pdf_path, pages=self.pages)
        self.table = tables[0]

    def to_csv(self, filename):
        self.table.to_csv(filename)

    def to_excel(self, filename):
        df = self.table.df
        writer = pd.ExcelWriter(filename)
        df.to_excel(writer, index=False)
        writer.save()

    def to_json(self, filename):
        data = self.table.to_json()
        with open(filename, 'w') as f:
            f.write(data)
