import os


def get_home_dir():
    return os.path.expanduser("~")


def get_log_path():
    return os.path.join(get_home_dir(), "logs/")