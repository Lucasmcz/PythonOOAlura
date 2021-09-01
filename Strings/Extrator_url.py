class Extrator_url():
    def __init__(self,url):
        self.url = url.strip()
        self.valida_url()
    def sanitiza_url(self,url):
        return url.strip()

    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL Está vazia ")

    def get_url_base(self):
        indice_interrogação = self.url.find("?")
        base = self.url[0:indice_interrogação]  # Do inicio até certa posição
        return base

    def get_url_parametros(self):
        indice_interrogação = self.url.find("?")
        parametros = self.url[indice_interrogação+1:]
        return parametros

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
url_youtube = Extrator_url("youtube.com/watch?v=QArog-oWuDk&t=3s")
base = url_youtube.get_url_base()
print(base)
parametros = url_youtube.get_url_parametros()
print(parametros)
v = url_youtube.valor_parametro()
print(v)
