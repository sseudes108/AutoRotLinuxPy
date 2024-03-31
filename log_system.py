import subprocess
import datetime

from auto_rot_lib import catch_error


def gerar_log():
    processo = ["cat", "/var/log/auth.log", "|", "grep", "-i", "ssh"]
    data = datetime.datetime.now().strftime('%Y-%m-%d')
    with open("new_log.txt", "w", encoding='utf-8') as new_log_file:
        new_log_file.write(data)
        resultado = subprocess.run(processo, stdout=new_log_file, stderr=subprocess.PIPE)
        catch_error(resultado, str(__name__))

gerar_log()
