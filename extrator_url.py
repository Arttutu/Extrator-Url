import re


class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanetizacao(url)
        self.validacao()

    @staticmethod
    def sanetizacao(url):
        if type(url) == str:
            return url.strip()  # remove caracteres especias dos lados do textos
        else:
            return ""

    def validacao(self):

        if not self.url:
            raise ValueError("A URL está vazia")  # raise ValueError, retorna um erro no programa
        nome = self.get_nome_do_site()
        url_padrao = re.compile(
            "(http(s)?://)?(www.)?{}(.com)(.br)?".format(nome))  # () tem que ser igual  [] qualquer valor de dentro
        url_valida = url_padrao.match(self.url)  # math verifica se o tezto está de acordo ncom o padrão

        if not url_valida:
            raise ValueError("A URL não é valida")

    def get_nome_do_site(self):

        indice_separador = self.url.find(".com")
        nome = self.url[:indice_separador]
        return nome

    def get_url_base(self):
        indice_separatorio = self.url.find(
            "?")  # método find encontra um caracter ou texto dentro de uma string e passa sua posição inicial
        url_base = self.url[:indice_separatorio]
        return url_base

    def get_url_parametro(self):
        indice_separatorio = self.url.find("?")
        url_parametro = self.url[indice_separatorio + 1:]
        return url_parametro

    def get_busca_parametro(self, parametro):
        parametro_busca = parametro
        url_parametro_busca = self.get_url_parametro().find(parametro_busca)
        indice_valor = url_parametro_busca + len(parametro_busca) + 1
        indice_e = self.get_url_parametro().find('&', indice_valor)

        if indice_e == -1:
            url_valor = self.get_url_parametro()[indice_valor:]
        else:
            url_valor = self.get_url_parametro()[indice_valor:indice_e]

        return url_valor

    def get_converte(self, valor):
        convert = int(valor) / 5.52

        return convert

    # método especial predfinidios por todo objeto, chamados indiretamente
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametro() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


# extrator_url = extrator_url("'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100")
url = "https://alura.com.br/cambio?moedaDestino=Dolar&MoedaOrigem=real&quantidade=5"
extrator_url = ExtratorUrl(url)
quantidade = extrator_url.get_busca_parametro("quantidade")
print(f"valor em real é ${quantidade}")
valor_convertido = extrator_url.get_converte(quantidade)
print(f"valor em dolar é {round(valor_convertido,2)}$" )
# extrator_url2 = ExtratorUrl(url)
# print(extrator_url)
# print(extrator_url == extrator_url2)
