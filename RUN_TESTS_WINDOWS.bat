@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  where py >nul 2>nul
  if %errorlevel%==0 (set PYTHON=py -3) else (set PYTHON=python)
  %PYTHON% -m venv .venv
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r server\requirements.txt
cd server
python manage.py check
python manage.py test --verbosity 2
pause
