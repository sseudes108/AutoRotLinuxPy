import subprocess

def apt_update():
    comando = ["sudo", "apt", "update"]
    subprocess.run(comando)


apt_update()