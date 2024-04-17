from selenium import webdriver

# Inicializa o navegador Firefox
driver = webdriver.Firefox()

# Abre a URL desejada
driver.get("https://nostarch.com/automatestuff2")

# Encontra o elemento usando o seletor CSS
elem2 = driver.find_element_by_css_selector(
    "#edit-attributes-1 > div:nth-child(1) > label"
)

# Obtém o texto do elemento
print(elem2.text)

# Encontra o elemento de entrada de texto usando o seletor CSS
elem = driver.find_element_by_css_selector(
    "div.logo-wrapper:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
)

# Encontra todos os elementos <p> na página
elems = driver.find_elements_by_css_selector("p")

# Encontra o elemento de entrada de texto para pesquisa
searchElem = driver.find_element_by_css_selector(
    "div.logo-wrapper:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
)

# Insere texto no elemento de entrada de texto e envia o formulário
searchElem.send_keys("Olá")
searchElem.send_keys(Keys.RETURN)  # Envio do formulário pressionando a tecla Enter

# Fecha o navegador
driver.quit()
