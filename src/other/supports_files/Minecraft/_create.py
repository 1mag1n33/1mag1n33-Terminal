import os
from src.other.supports_files.Minecraft.types.Vanilla import urls
from src.other.commands.fun.minecraft import server_name, version, memory as mem

class Create():
    def __init__(self):
        pass
    
    path = f'Mc_Servers/{server_name}'
    
    if not os.path.exists(path):
        os.makedirs(path)
    
    Download_path = path
     # Generate eula.txt file
    eula_path = os.path.join(Download_path[0], "eula.txt")
    with open(eula_path, 'w') as f:
        f.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n")
        f.write("eula=true\n")

    java_path = os.environ.get('JAVA_HOME')

    # Generate run.bat file
    run_path = os.path.join(Download_path[0], "run.bat")
    with open(run_path, 'w') as f:
        l1 = "@ECHO OFF\n"
        l2 = "SET BINDIR=%~dp0\n"
        l3 = 'CD /D "%BINDIR%"\n'
        l4 = f'"{java_path}\\bin\\java" -Xmx{mem}M -Xms{mem}M -jar {type}_{version}.jar nogui\n"'
        l5 = "PAUSE\n"
        f.write(l1 + l2 + l3 + l4 + l5)

    # Download server jar file
    if version in urls:
        url = urls[version]
        jar_file_path = os.path.join(Download_path[0], f'{type}_{version}.jar')
        os.system(f'curl -o "{jar_file_path}" "{url}"')
    else:
        print(f"Error: Version {version} not found in urls")