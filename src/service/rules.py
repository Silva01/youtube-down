import os
from src.service import download


class Rules:

    def download(self, param, path, type):
        if param == "arq":
            urls = self.__obtain_url_file(path)
            for url in urls:
                self.__download_youtube(type, [url])
        else:
            self.__download_youtube(type, [path])

    def __download_youtube(self, type, url=[]):
        youtube = download.Download()
        if type == "mp3":
            youtube.mp3(url)
        elif type == "mp4":
            youtube.mp4(url)
        else:
            print("Parametro inválido")

    @staticmethod
    def excluir_webm(type):
        if type == "mp3":
            dir = os.listdir(os.getcwd())
            for file in dir:
                if file.find(".webm") > -1:
                    os.remove(file)

    @staticmethod
    def __obtain_url_file(path):
        dados = []
        arq = open(path, 'r')
        for linha in arq:
            dados.append(linha.rstrip('\n'))
        arq.close()
        return dados
