import re
'''
Verifica se a base da URL está de acordo com o padrão correto.
Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio
Exemplos de URL inválidas:
    https://bytebank/cambio
    http://bytebank.naoexiste/cambio
    ht:bytebank.naoexiste/cambio
'''
class Extrator_url():
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL Está vazia ")
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com?(.br)?/cambio')
        padrao_url.match('.......')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é valida")

    def get_url_base(self):
        indice_interrogação = self.url.find("?")
        base = self.url[0:indice_interrogação]  # Do inicio até certa posição
        return base

    def get_url_parametros(self):
        indice_interrogação = self.url.find("?")
        parametros = self.url[indice_interrogação+1:]
        return parametros

    def __len__(self):
        return len(self.url)

    def valor_parametro(self):
        indice_interrogação = self.url.find("?")
        parametrodebusca = "v"
        indicedebusca = self.url.find(parametrodebusca)
        parametros = self.url[indice_interrogação + 1:]  # Ate o final da String
        # print(f"{parametros}")
        indice_valor = indicedebusca + len(parametrodebusca) + 1  # indice do parametro
        #print(indice_valor)
        indicedoe = self.url.find("&", indice_valor)
        if (indicedoe == -1):
            valor = self.url[indice_valor:]
        else:
            valor = self.url[indice_valor:indicedoe]
        return valor
url_youtube = Extrator_url("http://www.bytebank.com.br/cambio")
print(url_youtube.__len__())

'''
base = url_youtube.get_url_base()
print(base)
parametros = url_youtube.get_url_parametros()
print(parametros)
v = url_youtube.valor_parametro()
print(v)
'''
