import json
import os
from src.other.commands.fun.Minecraft._create import Create

class Run():
    def __init__(self):
        
        self.port = Create.port    
        self.server_name = Create.server_name
        self.path = f'Mc_Servers/{self.server_name}'
        self.version = Create.version
        self.memory = Create.memory
        self.java_path = Create.java_path
        
        
    def Start(self):
        run_path = os.path.join(self.path, "run.bat")
        print (run_path)
        with open(run_path, 'w') as f:
            l1 = "@ECHO OFF\n"
            l2 = "SET BINDIR=%~dp0\n"
            l3 = 'CD /D "%BINDIR%"\n'
            l4 = f'"{self.java_path}\\bin\\java" -Xmx{self.memory}M -Xms{self.memory}M -jar {self.version}.jar nogui --port {self.port}\n'
            l5 = "PAUSE\n"
            f.write(l1 + l2 + l3 + l4 + l5)
            
        os.startfile(run_path)
        