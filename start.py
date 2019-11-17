import click
import sys
from src.service.rules import Rules
from loguru import logger


@click.command()
@click.option("--type", help="Tipo do vídeo a ser baixado, mp3 ou mp4")
@click.option("--param", help="Parametro de download, arq para arquivo ou a url a ser baixada")
@click.option("--path", default="-", help="Localização do arquivo, caso vazio obtem do diretório onde executado")
def main(type, param, path):
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
    rules = Rules()
    logger.info("Iniciando Download dos vídeos do youtube")
    logger.info("Opção escolhida foi {} Tipo de Download {} para o Path {}", type, param, path)
    rules.download(param, path, type)
    logger.info("Excluindo arquivos webm")
    rules.excluir_webm(type)
    logger.info("Finalizado")


if __name__ == '__main__':
    main()