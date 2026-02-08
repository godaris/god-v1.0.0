@echo off
REM GOD v1.0.0 - Windows Server Launcher

title GOD v1.0.0 Server

echo.
echo ====================================================================
echo    GOD v1.0.0 - Starting Server
echo ====================================================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python found!
echo.

if not exist "index.html" (
    echo [ERROR] index.html not found!
    echo Make sure you're running this from the GOD v1.0.0 folder
    echo.
    pause
    exit /b 1
)

echo [OK] Files found!
echo.
echo Starting server...
echo.

python server.py

pause
