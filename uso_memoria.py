import subprocess

from auto_rot_lib import get_memoria_log_path


def uso_memoria():
    # Define o diretorio principal
    log_path = get_memoria_log_path()

    processo1 = ["ps", "-e", "-o", "pid", "--sort", "-size"]
    processo2 = ["head", "-n", "11"]
    processo3 = ["grep", "[0-9]"]

    with open("{}processos_por_uso_memoria.txt".format(log_path), "w", encoding='utf-8') as log_file:
        ps_output = subprocess.Popen(processo1, stdout=subprocess.PIPE)
        head_output = subprocess.Popen(processo2, stdin=ps_output.stdout, stdout=subprocess.PIPE)
        grep_output = subprocess.Popen(processo3, stdin=head_output.stdout, stdout=log_file)

        # Espera a conclusão dos processos
        ps_output.wait()
        head_output.wait()
        grep_output.wait()

        processos = ler_numeros_do_arquivo("{}processos_por_uso_memoria.txt".format(log_path))

        for processo in processos:
            nome_processo = ["ps", "-p", "{}".format(processo), "-o", "comm="]
            nome_output = subprocess.Popen(nome_processo, stdout=subprocess.PIPE, text=True)
            nome_output, _ = nome_output.communicate()

            data_processo = ["echo", "-n", "date", "+%F,", "%H:", "%M:"]
            data_output = subprocess.Popen(data_processo, stdout=subprocess.PIPE, text=True)
            data_output, _ = data_output.communicate()

            # echo - n $(date +%F, %H: %M: %S,) >> "log/$nome_processo.log"
            # tamanho_processo =$(ps - p $pid -o size | grep[0-9])
            # echo
            # "$(bc <<< "
            # scale = 2;$tamanho_processo / 1024
            # ") MB" >> "log/$nome_processo.lo

            # Remove espaços em branco e quebras de linha do resultado
            nome_output = nome_output.strip()
            data_output = data_output.strip()

            # Salva o resultado em um arquivo com o nome correspondente ao processo
            with open("{}{}.txt".format(log_path, nome_output), "w", encoding='utf-8') as arquivo:
                arquivo.write("{},{}".format(data_output, nome_output))

    # apagar_log_inicial("{}processos_por_uso_memoria.txt".format(log_path))


def apagar_log_inicial(caminho_arquivo):
    processo = ["rm", "{}".format(caminho_arquivo)]
    subprocess.Popen(processo, stdout=subprocess.PIPE)


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
            numero = int(linha_limpa)
            numeros.append(numero)

    return numeros


uso_memoria()

