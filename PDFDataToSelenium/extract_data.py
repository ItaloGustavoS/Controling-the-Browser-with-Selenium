import pymupdf  # Importa pymupdf diretamente

# Caminho para o seu PDF
pdf_path = r"C:\Users\Felipe LM\Documents\GitHub\Controling-the-Browser-with-Selenium\PDFDataToSelenium\PDFs\PDF Felipe.PDF"


# Função para extrair dados específicos do PDF
def extract_data_from_pdf(pdf_path):
    extracted_data = {}

    # Palavras-chave para busca e inicialização dos campos
    keywords = {
        "Empresa": "Empresa",
        "Cnpj:": "Cnpj",
        "Ie:": "Ie",
        "Endereço": "Endereço",
        "Bairro": "Bairro",
        "Cidade": "Cidade",
        "Estado": "Estado",
        "Número do Pedido": "Número do Pedido",
        "Código": "Código",
        "Fornecedor": "Fornecedor",
    }

    # Abrir o PDF usando pymupdf diretamente
    with pymupdf.open(pdf_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            text = page.get_text("text")

            # Procurar cada palavra-chave no texto da página
            for field, keyword in keywords.items():
                try:
                    # Encontra o índice de início e o valor após a palavra-chave
                    start_index = text.index(keyword) + len(keyword)
                    extracted_value = text[
                        start_index : text.index("\n", start_index)
                    ].strip()
                    extracted_data[field] = extracted_value
                except ValueError:
                    # Se a palavra-chave não for encontrada na página, passa para a próxima
                    continue

    return extracted_data


# Executar a função e exibir os dados extraídos
data = extract_data_from_pdf(pdf_path)
print("Dados extraídos:", data)
