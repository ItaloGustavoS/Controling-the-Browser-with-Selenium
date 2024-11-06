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
            if "Empresa" in text:
                empresa_index = text.index("Empresa") + len("Empresa")
                extracted_data["Empresa"] = text[
                    empresa_index : text.index("\n", empresa_index)
                ].strip()

            if "Cnpj:" in text:
                cnpj_index = text.index("Cnpj:") + len("Cnpj:")
                extracted_data["Cnpj"] = text[
                    cnpj_index : text.index("\n", cnpj_index)
                ].strip()

            # Adicione mais palavras-chave conforme a necessidade
            if "Ie:" in text:
                ie_index = text.index("Ie:") + len("Ie:")
                extracted_data["Ie"] = text[
                    ie_index : text.index("\n", ie_index)
                ].strip()

            if "Endereço" in text:
                endereco_index = text.index("Endereço") + len("Endereço")
                extracted_data["Endereço"] = text[
                    endereco_index : text.index("\n", endereco_index)
                ].strip()

            if "Bairro" in text:
                bairro_index = text.index("Bairro") + len("Bairro")
                extracted_data["Bairro"] = text[
                    bairro_index : text.index("\n", bairro_index)
                ].strip()

            if "Cidade" in text:
                cidade_index = text.index("Cidade") + len("Cidade")
                extracted_data["Cidade"] = text[
                    cidade_index : text.index("\n", cidade_index)
                ].strip()

            if "Estado" in text:
                estado_index = text.index("Estado") + len("Estado")
                extracted_data["Estado"] = text[
                    estado_index : text.index("\n", estado_index)
                ].strip()

            if "Número do Pedido" in text:
                numero_pedido_index = text.index("Número do Pedido") + len(
                    "Número do Pedido"
                )
                extracted_data["Número do Pedido"] = text[
                    numero_pedido_index : text.index("\n", numero_pedido_index)
                ].strip()

            if "Código" in text:
                codigo_index = text.index("Código") + len("Código")
                extracted_data["Código"] = text[
                    codigo_index : text.index("\n", codigo_index)
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
