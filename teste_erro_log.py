import subprocess

def run_command():
    # Comando a ser executado
    comando = ["ls", "/diretorio/inexistente"]  # Comando que resultará em um erro

    # Executar o comando usando subprocess.run
    resultado = subprocess.run(comando, capture_output=True, text=True)

    # Verificar se ocorreu um erro
    if resultado.returncode != 0:
        # Imprimir a saída de erro
        print("Erro:", resultado.stderr)
    else:
        # Imprimir a saída padrão (stdout)
        print("Saída:", resultado.stdout)

# Chamar a função para executar o comando
run_command()