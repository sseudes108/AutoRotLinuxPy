###################################################################
## Automatiza o git pull dos diretorios designados               ##
## Os scripts podem ser atualizados pelo IDE com mais facilidade ##
###################################################################
from auto_rot_lib import get_git_AutoRotLinuxPy_path

import subprocess

def puxar_repos():
    repositorios = [get_git_AutoRotLinuxPy_path()]

    print(repositorios)
    for _ in repositorios:

        entrar = ["cd", _]
        print(entrar)
        subprocess.run(entrar)

        comando = ["git pull"]
        print(comando)
        subprocess.run(comando)


puxar_repos()

