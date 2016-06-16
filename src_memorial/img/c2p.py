from os import system
from glob import glob


def comando(nome_arquivo):
	return "inkscape -D -z --file="+ nome_arquivo +".svg --export-pdf=" + nome_arquivo + ".pdf"


for nome_arquivo in glob("*.svg"):
	system(comando(nome_arquivo[:-4]))
