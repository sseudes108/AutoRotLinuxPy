##########################################################
## Faz a copia de tudo dentro de origem para o destino  ##
## nao copia o diretorio                                ##
##########################################################
## Os Diretorio são referenciados de auto_rot_lib.py    ##
## e passados no call de criar_backup                   ##
##########################################################

import glob
import os
import subprocess

from auto_rot_lib import catch_error


def criar_backup(origem, destino):
    #Coleta todos os arquivos dentro do diretorio origem
    arquivos_em_origem = glob.glob(os.path.join(origem, "*"))

    #Monta o comando cp
    comando = ["cp", "-r"] + arquivos_em_origem + [destino]

    print(comando)
    resultado = subprocess.run(comando, stderr=subprocess.PIPE)

    catch_error(resultado, "backup_rotina.py / Origem: {} Destino {}".format(origem, destino))
