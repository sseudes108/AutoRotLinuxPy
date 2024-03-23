###################################################################
## Automatiza o git pull dos diretorios designados               ##
## Os scripts podem ser atualizados pelo IDE com mais facilidade ##
###################################################################
from auto_rot_lib import autoRotLinuxPy_repo, catch_error, get_home_dir

import os
import subprocess

def puxar_repos():
    # definir novos repositorios em auto_rot_lib.py e adicionar à lista
    repositorios = [autoRotLinuxPy_repo()]

    for repo in repositorios:
        #Entra no repositorio
        repository = repo
        repo = os.path.join(get_home_dir(), "py_scripts/", repo)
        os.chdir(repo)

        # ATENÇÃO!! ELIMINA QUALQUER MUDANÇA NO REPO LOCAL!!
        # (MANTER AS MUDANÇAS E O PUSH NO IDE, NÃO NO SERVER !!)
        resultado = subprocess.run(["git", "reset", "--hard"], stderr=subprocess.PIPE)
        catch_error(resultado, "git_rotina-Reset-Dir-{}".format(repository))

        #Executa o comando
        resultado = subprocess.run(["git", "pull"], stderr=subprocess.PIPE)

        catch_error(resultado, "git_rotina-Pull-Dir-{}".format(repository))

puxar_repos()

