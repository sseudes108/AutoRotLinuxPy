#######################################################
## Faz a copia de arquivos criados com log_rotina.py ##
#######################################################
import os

from auto_rot_lib import get_log_path, get_backup_path
from backup_rotina import criar_backup

log_path = get_log_path()
log_backup_path = get_backup_path()

origem = os.path.splitdrive(log_path)
print(origem[1])
destino = os.path.split(log_backup_path)
print(destino)

criar_backup(log_path, log_backup_path)

