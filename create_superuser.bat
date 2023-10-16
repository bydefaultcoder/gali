@echo off
echo Creating Django superuser...
cd D:\gali
echo now in project ...
set VENV_PATH=env\Scripts\activate.bat

rem Check if the virtual environment's activate script exists
if exist %VENV_PATH% (
    call %VENV_PATH%
    echo Virtual environment activated.
) else (
    echo Virtual environment not found. Please check the VENV_PATH.
)
echo env on ...
set /p username= hp
set /p email= hp@gmail.com
set /p password=1234567890

echo Creating Django superuser...
python manage.py createsuperuser --username=%username% --email=%email%

echo Django superuser created successfully.
pause