##########################################################
## Faz a copia de tudo dentro de target para o destino  ##
## nao copia o diretorio                                ##
##########################################################

import glob
import os
import subprocess

def criar_backup(target, destino):
    #Cria devidamente a string para que o * seja reconhecido como wildcard
    arquivos = glob.glob(os.path.join(target, "*"))

    #Monta o comando cp
    comando = ["cp", "-r"] + arquivos + [destino]

    subprocess.run(comando)