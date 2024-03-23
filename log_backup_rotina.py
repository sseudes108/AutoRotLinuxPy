#######################################################
## Faz a copia de arquivos criados com log_rotina.py ##
#######################################################
import os

from auto_rot_lib import get_log_path, get_backup_path
from backup_rotina import criar_backup

log_path = get_log_path()
log_backup_path = get_backup_path()

origem = os.path.split(log_path)
print(origem)
destino = os.path.split(log_backup_path)
print(destino)

criar_backup(log_path, log_backup_path)

