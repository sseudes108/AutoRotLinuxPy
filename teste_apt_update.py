import subprocess

def upgrade_packages():
    # Comando para atualizar os pacotes usando apt upgrade
    comando = ["sudo", "apt", "upgrade", "-y"]

    # Executar o comando usando subprocess
    processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

    # Enviar "yes" para a entrada padrão (stdin)
    stdout, stderr = processo.communicate(input=b"yes\n")

    # Capturar a saída do processo
    output = stdout.decode("utf-8")
    error = stderr.decode("utf-8")

    # Verificar se houve erros durante a execução do comando
    if processo.returncode != 0:
        print("Erro ao executar apt upgrade:", error)
    else:
        print("Pacotes atualizados com sucesso:", output)


# Chamar a função para atualizar os pacotes
upgrade_packages()