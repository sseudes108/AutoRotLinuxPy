import subprocess
from auto_rot_lib import catch_error


def run_command():
    # Comando a ser executado
    comando = ["ls", "/diretorio/inexistente"]  # Comando que resultará em um erro

    # Executar o comando usando subprocess.run
    resultado = subprocess.run(comando, capture_output=True, text=True)

    catch_error(resultado, "teste_erro_log.py")


# Chamar a função para executar o comando
run_command()

