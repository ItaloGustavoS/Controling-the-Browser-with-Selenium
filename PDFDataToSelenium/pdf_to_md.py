import pymupdf  # Para extrair o conteúdo do PDF
from markdownify import markdownify as md


def pdf_to_markdown(pdf_path, md_path):
    # Abrir o arquivo PDF e extrair o conteúdo
    with pymupdf.open(pdf_path) as pdf_file:
        content = ""
        for page_num in range(pdf_file.page_count):
            page = pdf_file[page_num]
            content += page.get_text()

    # Converter o conteúdo para Markdown
    md_content = md(content)

    # Salvar o conteúdo no arquivo Markdown
    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(md_content)

    print(f"Conteúdo salvo em {md_path}")


# Exemplo de uso para testes
pdf_to_markdown("seu_arquivo.pdf", "seu_arquivo.md")
