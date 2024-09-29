from PIL import Image
import requests
from io import BytesIO

# URL da imagem que você quer converter
image_url = "https://example.com/image.jpg"

# Fazer o download da imagem da web
response = requests.get(image_url)

# Abrir a imagem usando BytesIO
img = Image.open(BytesIO(response.content))

# Converter a imagem para PNG e salvar
img.save("imagem_convertida.png", "PNG")

print("Imagem convertida e salva como imagem_convertida.png")
