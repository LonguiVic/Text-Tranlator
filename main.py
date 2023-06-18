from googletrans import Translator


def traduzir_texto(texto, idioma_destino):
    translator = Translator(service_urls=['translate.google.com'])
    traducao = translator.translate(texto, dest=idioma_destino)
    return traducao.text


texto = input("Digite o texto a ser traduzido: ")
idioma_destino = input("Digite o idioma para o qual deseja traduzir: ")

traducao = traduzir_texto(texto, idioma_destino)
print("Texto traduzido:", traducao)
