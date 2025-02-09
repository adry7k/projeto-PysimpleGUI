from PIL import Image

imagem = Image.open('Logo_Ufra.png')

tamanho = (50,50)
imagem.thumbnail(tamanho)
imagem.save('LogoUfra.png')
