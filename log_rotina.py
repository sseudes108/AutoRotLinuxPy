##########################################################
## Pega as 10 utimas linhas de syslog                   ##
## Arquivo target pode ser alterado na lista "processo" ##
##########################################################

import subprocess
import os


def criar_log():
    #Define os diretorios
    home_dir = os.path.expanduser("~")
    log_path = os.path.join(home_dir, "logs/")

    #Verifica o Log e acrescenta 1
    log = ler_log(log_path) + 1

    #Modifica o log para o novo valor acrescido
    with open("{}log.txt".format(log_path), "w", encoding='utf-8') as log_file:
        log_file.write("{}".format(log, end=""))

    #Busca e escreve o resultado sem passar pelo shell
    processo = ["tail", "-n", "10", "/var/log/syslog"]
    with open("{}log{}.txt".format(log_path, log), "w", encoding='utf-8') as new_log_file:
        subprocess.run(processo, stdout=new_log_file)

def ler_log(log_path):
    with open("{}log.txt".format(log_path), "r", encoding='utf-8') as log_file:
        log = log_file.read().strip()
        print("current log", log)
        log_file.close()
    return int(log)


criar_log()