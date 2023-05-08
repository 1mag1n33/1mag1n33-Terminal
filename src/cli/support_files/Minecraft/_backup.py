import shutil
import os
import time

from src.other.support_files.Minecraft._create import Create



class Backup():
    def __init__(self):
        
        self.server_name = Create().server_name
        self.path = f'Mc_Servers/Servers/{self.server_name}'
        self.backup_path = f'Mc_Servers/Backups/{self.server_name}'
    
    def create_backup(self):
        if not os.path.exists(self.backup_path):
            os.makedirs(self.backup_path)

        backup_folder = os.path.join(self.backup_path, time.strftime("%Y-%m-%d_%H-%M-%S"))
        os.makedirs(backup_folder)

        world_folder = os.path.join(self.path, 'world')
        shutil.copytree(world_folder, os.path.join(backup_folder, 'world'))
