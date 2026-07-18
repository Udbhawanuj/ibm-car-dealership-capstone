@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Run RUN_PROJECT_WINDOWS.bat first.
  pause
  exit /b 1
)
call .venv\Scripts\activate.bat
python scripts\generate_evidence.py --base-url http://127.0.0.1:8000
if errorlevel 1 (
  echo Evidence generation failed. Make sure the Django server is running.
  pause
  exit /b 1
)
echo.
echo Evidence files are ready inside the evidence folder.
pause
