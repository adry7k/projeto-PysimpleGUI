from PIL import Image

imagem = Image.open('question200.png')

tamanho = (300,300)
imagem.thumbnail(tamanho)
imagem.save('question300.png')

