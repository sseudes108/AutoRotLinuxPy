import os

def get_home_dir():
    return os.path.expanduser("~")

def get_log_path():
    return os.path.join(get_home_dir(), "logs/")

def get_backup_path():
    return os.path.join(get_home_dir(), "logs_backup/")

def get_git_AutoRotLinuxPy_path():
    return os.path.join(get_home_dir(), "py_scripts/AutoRotLinuxPy")

def get_git_Ominifood_path():
    return os.path.join(get_home_dir(), "web/Omnifood")


