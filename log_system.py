import subprocess
import datetime

from auto_rot_lib import catch_error


def gerar_log():
    processo = ["cat", "auth.log", "|", "grep", "$HOSTNAME", "|", "awk", "-F", "$HOSTNAME", "'{print $HOSTNAME $2}'",
                "|", "grep", "ssh"]
    data = datetime.datetime.now().strftime('%Y-%m-%d')
    with open("new_log.txt", "w", encoding='utf-8') as new_log_file:
        new_log_file.write(data)
        resultado = subprocess.run(processo, stdout=new_log_file, stderr=subprocess.PIPE)
        catch_error(resultado, __name__)

gerar_log()
