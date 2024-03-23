import subprocess
from auto_rot_lib import catch_error


def upgrade_packages():
    # Comando para atualizar os pacotes usando apt upgrade
    comando = ["apt", "upgrade", "-y"]

    # Executar o comando usando subprocess
    resultado = subprocess.Popen(comando, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

    # Enviar "yes" para a entrada padrão (stdin)
    resultado.communicate(input=b"yes\n")

    catch_error(resultado, "apt_update_upgrade")


# Chamar a função para atualizar os pacotes
upgrade_packages()