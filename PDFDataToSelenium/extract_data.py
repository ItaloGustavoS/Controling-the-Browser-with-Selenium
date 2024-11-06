import pymupdf  # Certifique-se de que o pymupdf está instalado

# Caminho para o seu PDF
pdf_path = r"C:\Users\Felipe LM\Documents\GitHub\Controling-the-Browser-with-Selenium\PDFDataToSelenium\PDFs\PDF Felipe.PDF"


# Função para extrair dados do PDF
def extract_data_from_pdf(pdf_path):
    extracted_data = {
        "Empresa": "",
        "CNPJ": "",
        "IE": "",
        "Endereço": "",
        "Bairro": "",
        "Cidade": "",
        "Estado": "",
        "Número do Pedido": "",
        "Data do Pedido": "",
        "Itens do Pedido": [],
        "Total da Quebra": "",
        "Total Geral": "",
        "Condição de Pagamento": "",
        "Data de Entrega": "",
        "Total do Pedido": "",
        "Observações": "",
    }

    # Abrir o PDF
    with pymupdf.open(pdf_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            text = page.get_text("text")

            # Busca das principais informações com base em palavras-chave
            if "Empresa" in text:
                extracted_data["Empresa"] = extract_value(text, "Empresa", "\n")
            if "CNPJ" in text:
                extracted_data["CNPJ"] = extract_value(text, "CNPJ", "\n")
            if "Ie" in text:
                extracted_data["IE"] = extract_value(text, "Ie", "\n")
            if "Endereço" in text:
                extracted_data["Endereço"] = extract_value(text, "Endereço", "\n")
            if "Bairro" in text:
                extracted_data["Bairro"] = extract_value(text, "Bairro", "\n")
            if "Cidade" in text:
                extracted_data["Cidade"] = extract_value(text, "Cidade", "\n")
            if "Estado" in text:
                extracted_data["Estado"] = extract_value(text, "Estado", "\n")
            if "Número do Pedido" in text:
                extracted_data["Número do Pedido"] = extract_value(
                    text, "Número do Pedido", "\n"
                )
            if "Data do Pedido" in text:
                extracted_data["Data do Pedido"] = extract_value(
                    text, "Data do Pedido", "\n"
                )
            if "Total da Quebra" in text:
                extracted_data["Total da Quebra"] = extract_value(
                    text, "Total da Quebra", "\n"
                )
            if "Total Geral" in text:
                extracted_data["Total Geral"] = extract_value(text, "Total Geral", "\n")
            if "Condição de pagamento" in text:
                extracted_data["Condição de Pagamento"] = extract_value(
                    text, "Condição de pagamento", "\n"
                )
            if "Data entrega" in text:
                extracted_data["Data de Entrega"] = extract_value(
                    text, "Data entrega", "\n"
                )
            if "Total do Pedido" in text:
                extracted_data["Total do Pedido"] = extract_value(
                    text, "Total do Pedido", "\n"
                )

            # Extração dos itens do pedido (multilinhas com código, descrição, quantidade, etc.)
            extracted_data["Itens do Pedido"].extend(extract_items(text))

            # Extrair Observações
            if "Observações Gerais" in text:
                extracted_data["Observações"] = extract_value(
                    text, "Observações Gerais", "ENDERECO DE COBRANCA"
                ).strip()

    return extracted_data


# Função auxiliar para extrair o valor associado a uma palavra-chave
def extract_value(text, keyword, end_marker):
    try:
        start_index = text.index(keyword) + len(keyword)
        end_index = text.index(end_marker, start_index)
        return text[start_index:end_index].strip()
    except ValueError:
        return ""


# Função para extrair itens do pedido em forma de dicionário
def extract_items(text):
    items = []
    lines = text.splitlines()
    for line in lines:
        # Se a linha corresponde ao padrão de item (código, descrição, qtd, valor unitário, total)
        if "Produto:" in line or any(char.isdigit() for char in line):
            parts = line.split()  # Divide a linha em partes
            if len(parts) >= 5:
                item = {
                    "Código": parts[0],
                    "Descrição": " ".join(parts[1:-3]),
                    "Quantidade": parts[-3],
                    "Valor Unitário": parts[-2],
                    "Valor Total": parts[-1],
                }
                items.append(item)
    return items


# Executar a função e exibir os dados extraídos
data = extract_data_from_pdf(pdf_path)
print("Dados extraídos:", data)
