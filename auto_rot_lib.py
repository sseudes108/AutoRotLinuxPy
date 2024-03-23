import os


def get_home_dir():
    return os.path.expanduser("~")


def get_log_path():
    return os.path.join(get_home_dir(), "logs/")

def get_erros_log_path():
    return os.path.join(get_log_path(), "errors/")

def get_backup_path():
    return os.path.join(get_home_dir(), "logs_backup/")


def autoRotLinuxPy_repo():
    return os.path.join(get_home_dir(), "py_scripts/AutoRotLinuxPy")


