from PIL import Image

imagem = Image.open('ufra.png')

tamanho = (100,100)
imagem.thumbnail(tamanho)
imagem.save('ufra100.png')