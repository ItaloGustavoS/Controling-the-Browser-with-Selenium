import pymupdf  # PyMuPDF
from markdownify import markdownify as md


def pdf_to_markdown(pdf_path, md_path):
    # Abrir o arquivo PDF
    with pymupdf.open(pdf_path) as pdf_file:
        content = ""

        # Iterar pelas páginas e extrair o texto
        for page_num in range(pdf_file.page_count):
            page = pdf_file[page_num]
            content += page.get_text()

    # Converter o conteúdo para Markdown
    md_content = md(content)

    # Salvar no arquivo Markdown
    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(md_content)

    print(f"Conteúdo salvo em {md_path}")


# Exemplo de uso
pdf_to_markdown("seu_arquivo.pdf", "seu_arquivo.md")
