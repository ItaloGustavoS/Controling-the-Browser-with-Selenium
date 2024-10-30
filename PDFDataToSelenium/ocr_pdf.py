from pdf2image import convert_from_path
import pytesseract
import cv2
import numpy as np

# Caminho do Poppler (necessário para Windows)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Substitua pelo caminho real
)


def pdf_to_images(pdf_path):
    # Converte cada página do PDF em uma imagem
    images = convert_from_path(pdf_path)
    return images


def extract_text_from_region(image, x, y, w, h):
    # Extrai texto de uma região específica da imagem (coordenadas x, y, largura w, altura h)
    region = image[y : y + h, x : x + w]
    text = pytesseract.image_to_string(region)
    return text


def main(pdf_path):
    # Converte o PDF em imagens
    images = pdf_to_images(pdf_path)

    # Exemplo: Processar a primeira página do PDF
    # Converte a primeira página para um array numpy, que o OpenCV pode processar
    image = np.array(images[0])
    image = cv2.cvtColor(
        image, cv2.COLOR_RGB2BGR
    )  # Converte para BGR para uso com OpenCV

    # Definir coordenadas de regiões específicas (substitua com as coordenadas do seu PDF)
    nome_region = (100, 150, 300, 50)  # (x, y, largura, altura)

    # Extrair texto das regiões especificadas
    nome_text = extract_text_from_region(image, *nome_region)

    print("Nome extraído:", nome_text.strip())


# Caminho do PDF
pdf_path = r"C:\Users\Felipe LM\Documents\GitHub\Controling-the-Browser-with-Selenium\PDFDataToSelenium\PDFs\form_Sample.pdf"
main(pdf_path)
