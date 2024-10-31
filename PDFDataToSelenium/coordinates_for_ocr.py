import cv2
from pdf2image import convert_from_path
import numpy as np

# Variáveis globais para armazenar as coordenadas
drawing = False
ix, iy = -1, -1


# Função para desenhar retângulo e salvar as coordenadas
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, image

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y  # Início do retângulo

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp_img = (
                image.copy()
            )  # Imagem temporária para exibir retângulo ao arrastar o mouse
            cv2.rectangle(temp_img, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow("Imagem PDF", temp_img)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(image, (ix, iy), (x, y), (0, 255, 0), 2)
        cv2.imshow("Imagem PDF", image)

        # Calcula a largura e altura do retângulo
        w, h = abs(x - ix), abs(y - iy)
        print(f"Coordenadas (x, y, w, h): ({ix}, {iy}, {w}, {h})")


def display_pdf_page(pdf_path, page_num=0):
    # Converte a página do PDF em uma imagem
    images = convert_from_path(pdf_path, poppler_path=r"C:\poppler\bin")
    img = np.array(images[page_num])
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img


def resize_image(img, width=800, height=600):
    # Redimensiona a imagem para caber em uma janela de tamanho fixo
    return cv2.resize(img, (width, height))


# Caminho para o PDF e visualização da página
pdf_path = r"C:\Users\Felipe LM\Documents\GitHub\Controling-the-Browser-with-Selenium\PDFDataToSelenium\PDFs\form_Sample.pdf"
image = display_pdf_page(pdf_path, page_num=0)

# Redimensiona a imagem para um tamanho fixo (ajuste conforme necessário)
image = resize_image(image, width=800, height=600)

# Configura a janela e o mouse callback
cv2.namedWindow("Imagem PDF", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Imagem PDF", draw_rectangle)

cv2.imshow("Imagem PDF", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
