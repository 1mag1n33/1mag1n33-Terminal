@echo off

:menu
echo 1. Run the application
echo 2. Install the application
echo 3. Information
set /p choice=Enter choice: 

if %choice%==1 (
    python run.py
) else if %choice%==2 (
    cd src
    pip install -r req.txt
) else if %choice%==3 (
    cd src
    python info.py
) else (
    echo Invalid choice
    goto menu
)