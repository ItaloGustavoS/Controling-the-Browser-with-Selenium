import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.chrome.service import Service

# Definir os diretórios de log
log_dir = (
    "C:\\Users\\Felipe LM\\Documents\\GitHub\\CrewAi-Llama3.1\\testsWebAutomation\\Logs"
)


# Função para configurar o log
def configurar_logger():
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)  # Cria o diretório de logs, se não existir
    nome_log = os.path.join(
        log_dir, f'log_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt'
    )
    logging.basicConfig(
        filename=nome_log,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return nome_log


# Função para inicializar o WebDriver e abrir o navegador
def inicializar_navegador(chrome_driver_path):
    try:
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        logging.info("Navegador aberto com sucesso.")
        return driver
    except Exception as e:
        logging.error(f"Erro ao abrir o navegador: {e}")
        raise


# Função para interagir com o navegador (clicar e preencher campos)
def interagir_navegador(driver):
    try:
        # Clicar no botão "Entrar"
        xpath_botao_entrar = (
            "/html/body/div[3]/div/div[7]/div[1]/div[2]/div/div[2]/a[1]"
        )
        button = driver.find_element(By.XPATH, xpath_botao_entrar)
        driver.save_screenshot(
            "C:\\Users\\Felipe LM\\Documents\\GitHub\\CrewAi-Llama3.1\\testsWebAutomation\\Screenshots\\screenshot.png"
        )
        button.click()
        logging.info("Automação: botão -Entrar- clicado com sucesso.")

        # Aguardar até que o campo de login esteja clicável (tempo máximo de espera: 20 segundos)
        wait = WebDriverWait(driver, 20)
        xpath_campo_login = "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]"
        input_field = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_campo_login))
        )

        # Clicar no campo de login e enviar o texto
        input_field.click()  # Colocar o campo em foco
        input_field.send_keys("italo.senna@lm4tech.com")
        input_field.send_keys(Keys.ENTER)
        logging.info(
            "Automação: -Login- inserido e botão -Enter- apertado com sucesso no campo de entrada."
        )

        # Aguardar até que o campo de senha esteja clicável
        xpath_campo_senha = "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input"
        input_field = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_campo_senha))
        )

        # Clicar no campo de senha e enviar o texto
        input_field.click()  # Colocar o campo em foco
        input_field.send_keys("ItaloBR150699")
        input_field.send_keys(Keys.ENTER)
        logging.info(
            "Automação: -Senha- inserida e botão -Enter- apertado com sucesso no campo de senha."
        )

        # Aguardar até que o botão "Entrar" esteja clicável para continuar logado
        xpath_botao_confirmar = "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input"
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_botao_confirmar))
        )
        button.click()
        logging.info(
            "Automação: Botão -Entrar- apertado com sucesso na confirmação de -Continuar conectado?-."
        )

        # Aguardar até que a área de aplicativos esteja clicável
        xpath_area_aplicativos = (
            "/html/body/div[9]/div/div/div[2]/div[1]/div[1]/div[1]/div/button"
        )
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_area_aplicativos))
        )
        button.click()
        logging.info("Automação: Aberto a área dos aplicativos Office.")

        # Aguardar até que o botão do Controle de Atividades esteja clicável
        cssselector_abrir_controle_atividades = "#O365_AppTile_\/providers\/Microsoft\.PowerApps\/apps\/49d4e56e-adaa-4eb1-a6e1-78fe9b1d4ea0"
        input_field = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, cssselector_abrir_controle_atividades)
            )
        )
        input_field.click()
        logging.info("Automação: Clique no botão para abrir o Controle de Atividades.")

        # Aguardar até que o botão "Nova Atividade" esteja clicável
        cssselector_nova_atividade = "#publishedCanvas > div > div.app-canvas > div:nth-child(3) > div > div > div:nth-child(14) > div > div > div > div > button > div > div"
        button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, cssselector_nova_atividade))
        )
        button.click()
        logging.info("Automação: Clique no botão -Ferias-.")

    except Exception as e:
        logging.error(f"Erro ao interagir com o navegador: {e}")
        raise


# Função principal de execução da automação
def main():
    # Configurar o logger
    nome_log = configurar_logger()
    logging.info("Início da automação.")

    # Caminho onde o chromedriver está localizado
    chrome_driver_path = "C:\\Users\\Felipe LM\\Documents\\GitHub\\CrewAi-Llama3.1\\testsWebAutomation\\ChromeDriver\\chromedriver.exe"

    # Inicializar o navegador
    driver = inicializar_navegador(chrome_driver_path)

    try:
        # Acessar a URL principal
        driver.get("https://www.office.com/")
        logging.info("Site acessado com sucesso: https://www.office.com/")

        # Executar as interações no navegador
        interagir_navegador(driver)
    except Exception as e:
        logging.error(f"Ocorreu um erro durante a automação: {e}")
    finally:
        # Fechar o navegador após todas as interações
        driver.quit()
        logging.info("Navegador encerrado com sucesso.")

    # Informar o local do log
    print(f"Log salvo em: {nome_log}")


# Executar a função principal
if __name__ == "__main__":
    main()
