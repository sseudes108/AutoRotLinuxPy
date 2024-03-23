import subprocess
from auto_rot_lib import get_erros_log_path

def run_command():
    # Comando a ser executado
    comando = ["ls", "/diretorio/inexistente"]  # Comando que resultará em um erro

    # Executar o comando usando subprocess.run
    resultado = subprocess.run(comando, capture_output=True, text=True)

    # Verificar se ocorreu um erro
    if resultado.returncode != 0:
        # Imprimir a saída de erro
        print("Erro:", resultado.stderr)
        error_log_path = get_erros_log_path()

        erro = "Erro: " + resultado.stderr
        file = "teste_erro_log.py"

        with open("{}error-{}.txt".format(error_log_path, file), "w",
                  encoding="utf-8") as error_log:
            error_log.write(erro)

    else:
        # Imprimir a saída padrão (stdout)
        print("Saída:", resultado.stdout)

# Chamar a função para executar o comando
run_command()