import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Caminho para o XML gerado a partir do PDF
xml_path = r"C:\Users\Felipe LM\Documents\GitHub\Controling-the-Browser-with-Selenium\PDFDataToSelenium\PDFs\form_Sample.xml"


# Função para extrair dados específicos do XML com base nas coordenadas
def extract_fields_from_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Aqui você pode ajustar as coordenadas para encontrar os campos certos
    fields = {}
    for text in root.findall(".//text"):
        content = text.text.strip() if text.text else ""
        top = int(text.get("top", 0))
        left = int(text.get("left", 0))

        # Condições de exemplo: altere conforme as coordenadas dos campos no seu XML
        if 100 < left < 200 and 150 < top < 200:
            fields["nome"] = content
        elif 300 < left < 400 and 250 < top < 300:
            fields["endereco"] = content
        # Adicione mais condições para outros campos

    return fields


# Função para preencher formulário com Selenium
def fill_web_form(fields):
    driver = webdriver.Chrome()
    driver.get(
        "https://formsmarts.com/html-form-example"
    )  # Substitua pela URL do seu formulário

    # Espera a página carregar completamente
    time.sleep(3)

    # Preenche os campos com os dados extraídos do XML
    if "nome" in fields:
        driver.find_element(By.ID, "nome").send_keys(fields["nome"])
    if "endereco" in fields:
        driver.find_element(By.ID, "endereco").send_keys(fields["endereco"])

    # Finalize ou adicione qualquer outra ação no formulário
    time.sleep(2)  # Ajuste o tempo conforme necessário
    driver.quit()


# Extração dos dados a partir do XML
fields = extract_fields_from_xml(xml_path)
print("Campos extraídos:", fields)

# Preenchimento do formulário
fill_web_form(fields)
