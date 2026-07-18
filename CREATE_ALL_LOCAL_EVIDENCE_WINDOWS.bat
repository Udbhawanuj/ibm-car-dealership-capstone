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
python scripts\generate_evidence.py --start-server --base-url http://127.0.0.1:8000
if errorlevel 1 (
  echo Evidence generation failed.
  pause
  exit /b 1
)
echo.
echo DONE. Open the evidence folder.
pause
