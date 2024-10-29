import streamlit as st
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Função para configurar o navegador com o cookie e acessar o perfil
def setup_browser_with_cookies_and_access_profile(profile_url):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Maximizar a janela do navegador
    driver.maximize_window()

    # Abrir a página inicial do LinkedIn
    driver.get("https://www.linkedin.com")

    # Adicionar o cookie 'li_at' diretamente no código
    li_at_cookie = "AQEDATdB220FI4-bAAABkd2Em-EAAAGSJZoy7U0Ae-VgApffKYlRXIoZ-EnGNd9qDxj_MpYRbyHpqzD0xnGkmxEFe6B6Thyc9FBmtts9zqyjC0YmYvw7zSer9z01GR09hVs0SWe9nbeLRpoHX3SzBlXh"
    driver.add_cookie(
        {"name": "li_at", "value": li_at_cookie, "domain": ".linkedin.com"}
    )

    # Atualizar a página para usar os cookies adicionados
    driver.refresh()

    # Acessar a URL do perfil do candidato
    acessar_perfil_candidato(profile_url, driver)


# Função para acessar o perfil do LinkedIn e extrair as informações
def acessar_perfil_candidato(profile_url, driver):
    try:
        wait = WebDriverWait(driver, 10)

        # Acessar o perfil do candidato
        driver.get(profile_url)
        time.sleep(8)

        # Passo 1: Clicar no botão "ver mais" para expandir o conteúdo
        show_more_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//button[contains(@class, "inline-show-more-text__button")]',
                )
            )
        )
        driver.execute_script("arguments[0].click();", show_more_button)

        # Passo 2: Extrair o conteúdo desejado do perfil
        content_element = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[3]/div[3]/div/div/div",
                )
            )
        )
        content = content_element.text
        st.write(f"Conteúdo extraído: {content}")

        # Simular atraso antes de continuar
        time.sleep(8)

        # Novo passo: Clicar no botão para prosseguir antes de localizar o campo de mensagem
        prosseguir_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]/button",
                )
            )
        )
        driver.execute_script("arguments[0].click();", prosseguir_button)

        # Simular outro atraso antes de continuar
        time.sleep(8)

        # Passo 3: Localizar o campo de mensagem no LinkedIn
        message_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/div[3]/div[1]/div/div[1]",
                )
            )
        )

        # Gerar a mensagem e escrever no campo de mensagem em tempo real
        gerar_mensagem_llama_e_digitar(content, driver, message_field)

    except Exception as e:
        st.error(f"Erro ao acessar o perfil e realizar as ações: {e}")


# Função principal para gerar e enviar a mensagem via LLaMA 3.1 local com Ollama, simulando a digitação em tempo real
def gerar_mensagem_llama_e_digitar(profile_content, driver, message_field):
    try:
        # Definir a persona e o prompt personalizado
        persona_prompt = (
            f"Você está atuando como Rafaela, recrutadora da empresa LM4Tech. Seu objetivo é criar uma mensagem curta, direta e objetiva. "
            f"A mensagem deve começar com 'Olá, meu nome é Rafaela, recrutadora da empresa LM4Tech', seguida de um breve parágrafo demonstrando interesse no perfil do candidato.\n\n"
            f"Conteúdo do perfil do candidato:\n\n"
            f"{profile_content}\n\n"
            "A mensagem deve ser concisa e focada. Diga que a LM4Tech está à procura de profissionais com esse perfil e destaque brevemente "
            "como as qualificações e experiências do candidato se alinham às necessidades da empresa. Finalize a mensagem mostrando interesse em seguir para as próximas etapas."
        )

        st.info(
            "Gerando conteúdo com o LLaMA 3.1 via Ollama (simulando digitação em tempo real)..."
        )

        # Executa o Ollama localmente, enviando o prompt via stdin (entrada padrão)
        command = ["ollama", "run", "llama3.1"]
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Enviar o prompt para o processo
        process.stdin.write(persona_prompt)
        process.stdin.close()

        # Inicia a leitura contínua da saída do modelo LLaMA
        for line in iter(process.stdout.readline, ""):
            if line:
                for char in line.strip():
                    # Simular a digitação no campo de mensagem caractere por caractere
                    message_field.send_keys(char)
                    # Verificar se o caractere é pontuação para adicionar um espaço após
                    if char in [".", "!", "?"]:
                        message_field.send_keys(" ")
                    time.sleep(
                        0.05
                    )  # Intervalo entre as "teclas" para simular digitação realista

        # Espera o processo terminar
        process.stdout.close()
        process.wait()

        # Após terminar a digitação, espera 3 segundos e clica no botão de envio
        time.sleep(3)
        enviar_botao = driver.find_element(
            By.XPATH,
            "/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/footer/div[2]/div[1]/button",
        )
        enviar_botao.click()

    except Exception as e:
        st.error(f"Erro ao gerar a mensagem com o LLaMA 3.1 via Ollama: {e}")


# Interface do Streamlit
st.title("Recrutamento Automático com LLaMA 3.1 - LM4Tech")

# Formulário para inserir a URL do perfil do LinkedIn (cookie já inserido diretamente no código)
st.subheader("Insira a URL do perfil do LinkedIn do candidato")

profile_url = st.text_input("URL do Perfil do LinkedIn do Candidato")

if st.button("Acessar Perfil e Enviar Mensagem"):
    setup_browser_with_cookies_and_access_profile(profile_url)
