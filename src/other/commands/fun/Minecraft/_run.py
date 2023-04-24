import json
import os
from src.other.commands.fun.Minecraft._create import Create

class Run():
    def __init__(self):
         
        self.server_name = Create().server_name
        self.path = f'Mc_Servers/{self.server_name}'
        
        
    def Start(self):
        run_path = os.path.join(self.path, "run.bat")
        java_path = os.environ.get('JAVA_HOME')
        print (run_path)
        with open(run_path, 'w') as f:
            l1 = "@ECHO OFF\n"
            l2 = "SET BINDIR=%~dp0\n"
            l3 = 'CD /D "%BINDIR%"\n'
            l4 = f'"{java_path}\\bin\\java" -Xmx{Create().memory}M -Xms{Create().memory}M -jar {Create().version}.jar nogui --port {Create().port}\n'
            l5 = "PAUSE\n"
            f.write(l1 + l2 + l3 + l4 + l5)
            
        os.startfile(run_path)
        