###################################################################
## Automatiza o git pull dos diretorios designados               ##
## Os scripts podem ser atualizados pelo IDE com mais facilidade ##
###################################################################
from auto_rot_lib import get_git_AutoRotLinuxPy_path

import subprocess

def puxar_repos():
    repositorios = [get_git_AutoRotLinuxPy_path()]
    for _ in repositorios:
        entrar = ["cd", _]
        subprocess.run(entrar)

        comando = ["git pull"]
        subprocess.run(comando)