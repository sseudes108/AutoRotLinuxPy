import subprocess

from auto_rot_lib import get_log_path, catch_error


def uso_memoria():
    # Define o diretorio principal
    log_path = get_log_path()

    processo1 = ["ps", "-e", "-o", "pid", "--sort", "-size"]
    processo2 = ["head", "-n", "11"]
    processo3 = ["grep", "[0-9]"]

    with open("{}uso_memoria.txt".format(log_path), "w", encoding='utf-8') as log_file:
        ps_output = subprocess.Popen(processo1, stdout=subprocess.PIPE)
        head_output = subprocess.Popen(processo2, stdin=ps_output.stdout, stdout=subprocess.PIPE)
        grep_output = subprocess.Popen(processo3, stdin=head_output.stdout, stdout=log_file)

        # Espera a conclusão dos processos
        ps_output.wait()
        head_output.wait()
        grep_output.wait()

        processos = ler_numeros_do_arquivo("{}uso_memoria.txt".format(log_path))

        for processo in processos:
            processo4 = ["ps", "-p", "{}".format(processo), "-o", "comm="]
            with open("{}{}".format(log_path, processo), "w", encoding='utf-8') as processo_file:
                processo_output = subprocess.Popen(processo4, stdout=subprocess.PIPE)
                processo_output.wait()


def ler_numeros_do_arquivo(caminho_arquivo):
    # Lista para armazenar os números lidos
    numeros = []

    # Abre o arquivo para leitura
    with open(caminho_arquivo, "r") as arquivo:
        # Lê as linhas do arquivo
        linhas = arquivo.readlines()

        # Itera sobre as linhas
        for linha in linhas:
            # Remove espaços em branco e quebras de linha
            linha_limpa = linha.strip()

            # Tenta converter a linha em um número inteiro
            try:
                numero = int(linha_limpa)
                numeros.append(numero)
            except ValueError:
                # Se não for possível converter para inteiro, ignora a linha
                pass

    return numeros


uso_memoria()

