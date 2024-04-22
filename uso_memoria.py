import subprocess

from auto_rot_lib import get_log_path, catch_error


def uso_memoria():
    # Define o diretorio principal
    log_path = get_log_path()

    processo1 = ["ps", "-e", "-o", "pid"]
    processo2 = ["head", "-n", "11"]
    processo3 = ["grep", "[0-9]"]

    with open("{}uso_memoria.txt".format(log_path), "w", encoding='utf-8') as log_file:
        ps_output = subprocess.Popen(processo1, stdout=subprocess.PIPE)
        head_output = subprocess.Popen(processo2, stdin=ps_output.stdout, stdout=subprocess.PIPE)
        grep_output = subprocess.Popen(processo3, stdin=head_output.stdout, stdout=log_file)

        # Espera a conclusão dos processos
        ps_output.wait()
        head_output.wait()
        grep_output.wait()

        catch_error(ps_output, "PS.uso_memoria.py")
        catch_error(head_output, "HEAD.uso_memoria.py")
        catch_error(grep_output, "GREP.uso_memoria.py")


    # processo = ["ps", "-e", "-o", "pid", "|", "head", "-n", "11", "|", "grep", "[0-9]"]
    # with open("{}uso_memoria.txt".format(log_path), "w", encoding='utf-8') as log_file:
    #     resultado = subprocess.run(processo, stdout=log_file, stderr=subprocess.PIPE)
    #     catch_error(resultado, "uso_memoria.py")
    #     log_file.write("{}".format(resultado))


uso_memoria()