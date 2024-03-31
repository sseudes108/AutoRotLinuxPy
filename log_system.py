import subprocess
import datetime

from auto_rot_lib import catch_error


def gerar_log():
    processo = ["cat", "/var/log/auth.log"]
    filtro = ["grep", "-i", "ssh"]
    refino = ["cut", "-d", " ", "-f", "4-"]
    data = datetime.datetime.now().strftime('%Y-%m-%d')

    with open("new_log.txt", "w", encoding='utf-8') as new_log_file:
        new_log_file.write(data + ':')
        resultado = subprocess.run(processo, stdout=subprocess.PIPE)
        resultado = subprocess.run(filtro, input=resultado.stdout, stdout=subprocess.PIPE)
        resultado = subprocess.run(refino, input=resultado.stdout, stdout=new_log_file, stderr=subprocess.PIPE)
        catch_error(resultado, "log_system.py")


gerar_log()
