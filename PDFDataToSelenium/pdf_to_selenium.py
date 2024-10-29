import pymupdf
from markdownify import markdownify as md
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def pdf_to_text(pdf_path):
    # Abrir e extrair conteúdo do PDF
    with pymupdf.open(pdf_path) as pdf_file:
        content = ""
        for page_num in range(pdf_file.page_count):
            page = pdf_file[page_num]
            content += page.get_text()

    return content


def fill_form_with_selenium(content):
    # Configurar o driver do Selenium (exemplo com Chrome)
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Felipe LM\Documents\GitHub\Controling-the-Browser-with-Selenium\PDFDataToSelenium\ChromeDriver\chromedriver.exe"
    )
    driver.get("https://formsmarts.com/html-form-example")

    # Localize os campos e preencha com o conteúdo do PDF
    # Exemplo genérico:
    field1 = driver.find_element(By.ID, "campo1")
    field1.send_keys(content)  # Insira o texto do PDF

    # Adicione mais campos conforme necessário
    # field2 = driver.find_element(By.NAME, "campo2")
    # field2.send_keys(outra_informacao_extraida)

    # Submeter o formulário
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    time.sleep(5)  # Pausa para visualização (opcional)
    driver.quit()


# Extraia o conteúdo do PDF e preencha o formulário
pdf_content = pdf_to_text("seu_arquivo.pdf")
fill_form_with_selenium(pdf_content)
