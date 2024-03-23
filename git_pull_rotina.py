###################################################################
## Automatiza o git pull dos diretorios designados               ##
## Os scripts podem ser atualizados pelo IDE com mais facilidade ##
###################################################################
from auto_rot_lib import autoRotLinuxPy_repo, catch_error

import os
import subprocess

def puxar_repos():
    # definir novos repositorios em auto_rot_lib.py e adicionar à lista
    repositorios = [autoRotLinuxPy_repo()]

    for repo in repositorios:
        #Entra no repositorio
        os.chdir(repo)

        # ATENÇÃO!! ELIMINA QUALQUER MUDANÇA NO REPO LOCAL!!
        # (MANTER AS MUDANÇAS E O PUSH NO IDE, NÃO NO SERVER !!)
        subprocess.run(["git", "reset", "--hard"])

        #Executa o comando
        resultado = subprocess.run(["git", "pull"])

        catch_error(resultado, "git_pull_rotina.py / {}".format(repo))

puxar_repos()
