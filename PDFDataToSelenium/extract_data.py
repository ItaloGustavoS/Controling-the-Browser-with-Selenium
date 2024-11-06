import pymupdf

# Caminho para o seu PDF
pdf_path = r"C:\Users\Felipe LM\Documents\GitHub\Controling-the-Browser-with-Selenium\PDFDataToSelenium\PDFs\PDF Felipe.PDF"


# Função para extrair dados específicos do PDF
def extract_data_from_pdf(pdf_path):
    extracted_data = {}

    # Abrir o PDF
    with pymupdf.open(pdf_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            text = page.get_text("text")

            # Busca de campos por palavras-chave
            if "Nome:" in text:
                nome_index = text.index("Nome:") + len("Nome:")
                extracted_data["Nome"] = text[
                    nome_index : text.index("\n", nome_index)
                ].strip()

            if "Endereço:" in text:
                endereco_index = text.index("Endereço:") + len("Endereço:")
                extracted_data["Endereço"] = text[
                    endereco_index : text.index("\n", endereco_index)
                ].strip()

            # Adicione mais palavras-chave conforme a necessidade
            if "CNPJ:" in text:
                cnpj_index = text.index("CNPJ:") + len("CNPJ:")
                extracted_data["CNPJ"] = text[
                    cnpj_index : text.index("\n", cnpj_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

            if "Nome:" in text:
                nome_index = text.index("Nome:") + len("Nome:")
                extracted_data["Nome"] = text[
                    nome_index : text.index("\n", nome_index)
                ].strip()

            if "Endereço:" in text:
                endereco_index = text.index("Endereço:") + len("Endereço:")
                extracted_data["Endereço"] = text[
                    endereco_index : text.index("\n", endereco_index)
                ].strip()

            # Adicione mais palavras-chave conforme a necessidade
            if "CNPJ:" in text:
                cnpj_index = text.index("CNPJ:") + len("CNPJ:")
                extracted_data["CNPJ"] = text[
                    cnpj_index : text.index("\n", cnpj_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

            if "Fornecedor" in text:
                fornecedor_index = text.index("Fornecedor") + len("Fornecedor")
                extracted_data["Fornecedor"] = text[
                    fornecedor_index : text.index("\n", fornecedor_index)
                ].strip()

    return extracted_data


# Executar a função e exibir os dados extraídos
data = extract_data_from_pdf(pdf_path)
print("Dados extraídos:", data)
