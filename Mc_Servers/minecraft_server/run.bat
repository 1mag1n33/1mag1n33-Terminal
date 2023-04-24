@ECHO OFF
SET BINDIR=%~dp0
CD /D "%BINDIR%"
"C:\Program Files\Java\jdk-17.0.5\bin\java" -Xmx4000M -Xms4000M -jar latest.jar nogui --port 25565
PAUSE
