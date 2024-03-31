import subprocess
import datetime

from auto_rot_lib import catch_error


def gerar_log():
    processo = ["cat", "/var/log/auth.log"]
    filtro = ["grep", "-i", "ssh"]
    data = datetime.datetime.now().strftime('%Y-%m-%d')

    with open("new_log.txt", "w", encoding='utf-8') as new_log_file:
        new_log_file.write(data + '\n')
        resultado = subprocess.run(processo, stdout=subprocess.PIPE)
        resultado = subprocess.run(filtro, input=resultado.stdout, stdout=new_log_file, stderr=subprocess.PIPE, text=True)
        catch_error(resultado, "log_system.py")


gerar_log()
