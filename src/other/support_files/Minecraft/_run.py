import os
import threading
from time import sleep
from src.other.support_files.Minecraft._create import Create
from src.other.support_files.Minecraft._backup import Backup

class Run():
    def __init__(self):
         
        self.server_name = Create().server_name
        self.path = f'Mc_Servers/Servers/{self.server_name}'
        self.backup = f'Mc_Servers/Backups/{self.server_name}'
    
    @staticmethod
    def backup_thread(backup_interval, path):
        while True:
            Backup().create_backup()
            sleep(backup_interval * 60)
        
    def Start(self, backup_enabled):
        try:
            run_path = os.path.join(self.path, "run.bat")
            java_path = os.environ.get('JAVA_HOME')
            with open(run_path, 'w') as f:
                l1 = "@ECHO OFF\n"
                l2 = "SET BINDIR=%~dp0\n"
                l3 = 'CD /D "%BINDIR%"\n'
                l4 = f'"{java_path}\\bin\\java" -Xmx{Create().memory}M -Xms{Create().memory}M -jar {Create().version}.jar nogui --port {Create().port}\n'
                l5 = "PAUSE\n"
                f.write(l1 + l2 + l3 + l4 + l5)
                
            os.startfile(run_path)
            print(f"Running Minecraft server on port {Create().port}")
        except FileNotFoundError:
            print(f"Minecraft server with name '{Create().server_name}' not found")
        
        if backup_enabled:
            backup_interval = 1 # interval in minutes
            backup_thread = threading.Thread(target=Run.backup_thread, args=(backup_interval, self.path))
            backup_thread.daemon = True
            backup_thread.start()
