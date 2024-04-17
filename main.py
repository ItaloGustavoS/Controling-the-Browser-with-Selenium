# Importa as bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inicializa o navegador Firefox
driver = webdriver.Firefox()

# Abre a URL desejada
driver.get("https://nostarch.com/automatestuff2")

# Espera implicitamente por 5 segundos para garantir que a página seja carregada completamente
driver.implicitly_wait(5)

# Encontra o elemento usando o seletor CSS e obtém o texto do elemento
try:
    textpreco = driver.find_element(
        By.CSS_SELECTOR, value="#edit-attributes-1 > div:nth-child(1) > label"
    ).text
    print("Texto encontrado:", textpreco)
except Exception as e:
    print("Erro ao encontrar o elemento:", e)

# Encontra o elemento de entrada de texto para pesquisa
try:
    searchElem = driver.find_element(
        By.CSS_SELECTOR,
        value="div.logo-wrapper:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)",
    )
    # Insere texto no elemento de entrada de texto
    searchElem.send_keys("Olá")
    # Envio do formulário pressionando a tecla Enter
    searchElem.send_keys(Keys.RETURN)
except Exception as e:
    print("Erro ao encontrar o elemento de pesquisa:", e)
