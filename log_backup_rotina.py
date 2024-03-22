import subprocess

from auto_rot_lib import get_log_path, get_backup_path

def criar_backup():
    log_path = get_log_path()
    backup_path = get_backup_path()

    #pega os arquivos dentro do diretorio, nao o diretorio em si.
    comando = ["cp", "{}*".format(log_path), backup_path]
    subprocess.run(comando);