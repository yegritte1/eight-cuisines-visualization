@echo off
:: Set environment to support UTF-8 if possible
chcp 65001 >nul

echo ========================================
echo   BA DA CAI XI VISUALIZATION SYSTEM
echo ========================================
echo.
echo 1. Starting local server...
echo 2. Opening browser in 3 seconds...
echo.
echo URL: http://127.0.0.1:8000/menu.html
echo.
echo [Close this window to stop the server]
echo ========================================

:: Attempt to open the browser after a short delay
start /B "" cmd /c "timeout /t 3 /nobreak >nul && start http://127.0.0.1:8000/menu.html"

:: Run the python server
python -m http.server 8000

pause
