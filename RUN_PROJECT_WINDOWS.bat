@echo off
setlocal
cd /d "%~dp0"

echo ============================================================
echo DriveSphere Cars Dealership - Setup and Run
echo ============================================================

where py >nul 2>nul
if %errorlevel%==0 (
  set PYTHON=py -3
) else (
  set PYTHON=python
)

if not exist ".venv\Scripts\python.exe" (
  echo [1/5] Creating virtual environment...
  %PYTHON% -m venv .venv
  if errorlevel 1 goto :error
)

call .venv\Scripts\activate.bat

echo [2/5] Installing dependencies...
python -m pip install --upgrade pip
pip install -r server\requirements.txt
if errorlevel 1 goto :error

echo [3/5] Applying migrations...
cd server
python manage.py migrate --noinput
if errorlevel 1 goto :error

echo [4/5] Loading demo users, dealers, cars, and reviews...
python manage.py seed_demo
if errorlevel 1 goto :error

echo [5/5] Starting Django server...
echo.
echo App:   http://127.0.0.1:8000/
echo Admin: http://127.0.0.1:8000/admin/
echo Reviewer login: reviewer / Reviewer@123
echo Admin login:    root / Root@123
echo.
start "" cmd /c "timeout /t 4 /nobreak >nul & start http://127.0.0.1:8000/"
python manage.py runserver 0.0.0.0:8000
exit /b 0

:error
echo.
echo Setup failed. Read QUICK_START_HINDI.md or copy the error shown above.
pause
exit /b 1
