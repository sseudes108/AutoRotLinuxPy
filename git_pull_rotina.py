###################################################################
## Automatiza o git pull dos diretorios designados               ##
## Os scripts podem ser atualizados pelo IDE com mais facilidade ##
###################################################################
from auto_rot_lib import autoRotLinuxPy_repo

import os
import subprocess

def puxar_repos():
    repositorios = [autoRotLinuxPy_repo()]

    for repo in repositorios:
        #Entra no repositorio
        os.chdir(repo)

        # ELIMINA QUALQUER MUDANÇA NO REPO LOCAL!!
        # (LINUX - MANTER AS MUDANÇAS E O PUSH NO IDE !!!!)
        subprocess.run(["git", "reset", "--hard"])

        #Executa o comando
        subprocess.run(["git", "pull"])

puxar_repos()

