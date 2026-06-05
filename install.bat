@echo off
title DASH LOGIC - Installer
echo ============================================
echo      DASH LOGIC Bot - Dependency Installer
echo ============================================
echo.

set PYTHON_CMD=python
set PIP_CMD=pip

where python >nul 2>nul
if %errorlevel% neq 0 (
    for /d %%i in ("%USERPROFILE%\AppData\Local\Programs\Python\Python*") do (
        if exist "%%i\python.exe" (
            set PYTHON_CMD="%%i\python.exe"
            set PIP_CMD="%%i\Scripts\pip.exe"
            goto :found
        )
    )
    
    for /d %%i in ("%ProgramFiles%\Python*") do (
        if exist "%%i\python.exe" (
            set PYTHON_CMD="%%i\python.exe"
            set PIP_CMD="%%i\Scripts\pip.exe"
            goto :found
        )
    )
    
    for /d %%i in ("C:\Python*") do (
        if exist "%%i\python.exe" (
            set PYTHON_CMD="%%i\python.exe"
            set PIP_CMD="%%i\Scripts\pip.exe"
            goto :found
        )
    )
    
    echo [-] Python not found on your system!
    echo Please install Python and make sure to check "Add Python to PATH".
    echo Download link: https://www.python.org/downloads/
    echo.
    pause
    exit /b
)

:found
echo Found Python: %PYTHON_CMD%
echo.
echo Installing packages...
%PIP_CMD% install -r requirements.txt
echo.
echo ============================================
echo      Installation Completed!
echo ============================================
pause
