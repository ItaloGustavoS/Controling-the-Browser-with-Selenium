import subprocess
import os

# Caminho para o executável pdftohtml do Poppler
POPPLER_PATH = r"C:\Program Files (x86)\poppler\Library\bin\pdftohtml.exe"

# Caminho para o arquivo PDF de entrada e o XML de saída
pdf_path = r"C:\Users\Felipe LM\Documents\GitHub\Controling-the-Browser-with-Selenium\PDFDataToSelenium\PDFs\form_Sample.pdf"
xml_output_path = pdf_path.replace(".pdf", ".xml")


# Função para converter PDF para XML
def convert_pdf_to_xml(pdf_path, xml_output_path):
    command = [POPPLER_PATH, "-xml", pdf_path, xml_output_path]
    subprocess.run(command, check=True)
    print(f"Arquivo XML gerado em: {xml_output_path}")


# Executa a conversão
convert_pdf_to_xml(pdf_path, xml_output_path)

# Abre o XML gerado no editor padrão (opcional)
os.startfile(xml_output_path)
