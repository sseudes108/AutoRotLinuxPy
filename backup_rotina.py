##########################################################
## Faz a copia de tudo dentro de target para o destino  ##
## nao copia o diretorio                                ##
##########################################################

import subprocess


def criar_backup(target, destino):
    comando = ["cp", "{}*".format(target), destino]
    subprocess.run(comando)