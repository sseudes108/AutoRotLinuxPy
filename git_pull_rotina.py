###################################################################
## Automatiza o git pull dos diretorios designados               ##
## Os scripts podem ser atualizados pelo IDE com mais facilidade ##
###################################################################
from auto_rot_lib import get_git_AutoRotLinuxPy_path, get_git_Ominifood_path

import os
import subprocess

def puxar_repos():
    repositorios = [get_git_AutoRotLinuxPy_path(), get_git_Ominifood_path()]

    for repo in repositorios:
        #Entra no repositorio
        os.chdir(repo)

        #Executa o comando
        subprocess.run(["git", "pull"])

puxar_repos()

