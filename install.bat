@echo off

:menu
echo 1. Run the application
echo 2. Install the application
set /p choice=Enter choice: 

if %choice%==1 (
    python main.py
) else if %choice%==2 (
    pip install -r src/req.txt
) else (
    echo Invalid choice
    goto menu
)