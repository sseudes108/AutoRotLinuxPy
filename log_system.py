import subprocess
import datetime

from auto_rot_lib import catch_error


def ssh_server():
    processo = ["cat", "/var/log/auth.log"]
    filtro = ["grep", "-i", "ssh"]
    refino = ["cut", "-d", " ", "-f", "4-"]
    data = datetime.datetime.now().strftime('%Y-%m-%d')

    with open("auth_log_{}.txt".format(data), "w", encoding='utf-8') as new_log_file:
        resultado = subprocess.run(processo, stdout=subprocess.PIPE)
        resultado = subprocess.run(filtro, input=resultado.stdout, stdout=subprocess.PIPE)
        resultado = subprocess.run(refino, input=resultado.stdout, stdout=new_log_file, stderr=subprocess.PIPE)
        catch_error(resultado, "log_system.py")


ssh_server()
