import subprocess

from auto_rot_lib import get_log_path, catch_error


def uso_memoria():
    # Define o diretorio principal
    log_path = get_log_path()

    processo = ["ps", "-e", "-o", "pid", "|", "head", "-n", "11", "|", "grep", "[0-9]"]
    with open("uso_memoria.txt.txt", "w", encoding='utf-8') as log_file:
        resultado = subprocess.run(processo, stdout=log_file, stderr=subprocess.PIPE)
        catch_error(resultado, "uso_memoria.py")

