#######################################################
## Faz a copia de arquivos criados com log_rotina.py ##
#######################################################
import os

from auto_rot_lib import get_log_path, get_backup_path
from backup_rotina import criar_backup

log_path = get_log_path()
log_backup_path = get_backup_path()

origem = log_path.replace("/", "-")
print(origem)

criar_backup(log_path, log_backup_path)

