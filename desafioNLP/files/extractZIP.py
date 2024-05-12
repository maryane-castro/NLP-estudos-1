import zipfile

class ExtratorZip:
    def __init__(self, arquivo_zip, pasta_destino):
        self.arquivo_zip = arquivo_zip
        self.pasta_destino = pasta_destino

    def extrair(self):
        with zipfile.ZipFile(self.arquivo_zip, 'r') as zip_ref:
            zip_ref.extractall(self.pasta_destino)
