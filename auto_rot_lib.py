import datetime
import os

def get_home_dir():
    return os.path.expanduser("~")


def get_log_path():
    return os.path.join(get_home_dir(), "Scripts/logs/")

def get_memoria_log_path():
    return os.path.join(get_home_dir(), "Scripts/logs/uso_memoria/")

def get_erros_log_path():
    return os.path.join(get_log_path(), "errors/")


def get_backup_path():
    return os.path.join(get_home_dir(), "logs_backup/")

def autoRotLinuxPy_repo():
    return "AutoRotLinuxPy"


def catch_error(resultado, file_name):
    if resultado.returncode != 0:
        # Imprimir a saída de erro
        print("Erro:", resultado.stderr)
        error_log_path = get_erros_log_path()
        print(error_log_path)
        print(file_name)
        data_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        erro = "{} - Erro: {} - {}".format(data_hora, resultado.stderr, file_name)

        with open("{}err-{}.txt".format(error_log_path, file_name), "w",
                  encoding="utf-8") as error_log:
            error_log.write(erro + "\n")
