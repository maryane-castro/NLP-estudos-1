from files.extractZIP import ExtratorZip
from files.regularExpression import PDFExtractor
from files.chatBOT import DataProcessor

def main():
    # Extrair arquivos ZIP
    extrator = ExtratorZip("ativos.zip", "ativos")
    extrator.extrair()

    # Extrair texto de arquivos PDF e salvar em CSV
    extrator_pdf = PDFExtractor("ativos", "output.csv")
    extrator_pdf.scrape_pdf_directory()

    # Processar dados do CSV para JSON e realizar consultas
    processador = DataProcessor("output.csv")
    processador.read_csv_to_json()
    processador.write_json("output.json")
    processador.read_json("output.json")
    results = processador.query_data("Qual é o patrimônio líquido da ELTROBRAS?")
    print(results)

if __name__ == "__main__":
    main()
