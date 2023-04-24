import os
import json

from src.other.commands.fun.Minecraft.types.Vanilla import urls

class Create():
    def __init__(self):
        server_path = 'src/other/support_files/server_config.json'
        with open(server_path, 'r') as f:
            config = json.load(f)
        
        self.version = config['version']
        self.server_name = config['server_name']
        self.memory = config['memory']
        self.port = config['port']
        self.path = f'Mc_Servers/{self.server_name}'
        self.java_path = os.environ.get('JAVA_HOME')

    def generate_files(self):

        if not os.path.exists(self.path):
            os.makedirs(self.path)
        
        # Generate eula.txt file
        eula_path = os.path.join(self.path, "eula.txt")
        if not os.path.exists(eula_path):    
            with open(eula_path, 'w') as f:
                f.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n")
                f.write("eula=true\n")

        

        # Generate run.bat file
        run_path = os.path.join(self.path, "run.bat")
        with open(run_path, 'w') as f:
            l1 = "@ECHO OFF\n"
            l2 = "SET BINDIR=%~dp0\n"
            l3 = 'CD /D "%BINDIR%"\n'
            l4 = f'"{self.java_path}\\bin\\java" -Xmx{self.memory}M -Xms{self.memory}M -jar {self.version}.jar nogui --port {self.port}\n'
            l5 = "PAUSE\n"
            f.write(l1 + l2 + l3 + l4 + l5)

        # Download server jar file
        if self.version in urls:
            url = urls[self.version]
            jar_file_path = os.path.join(self.path, f'{self.version}.jar')
            os.system(f'curl -o "{jar_file_path}" "{url}"')
        else:
            print(f"Error: Version {self.version} not found in urls")
