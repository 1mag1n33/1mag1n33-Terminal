@echo off

:menu
echo 1. Run the application
echo 2. Install the application
set /p choice=Enter choice: 

if %choice%==1 (
    python main.py
) else if %choice%==2 (
    cd src
    pip install -r req.txt
) else (
    echo Invalid choice
    goto menu
)