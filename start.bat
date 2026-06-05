@echo off
title DASH LOGIC - 24/7 Voice Bot

set PYTHON_CMD=python

where python >nul 2>nul
if %errorlevel% neq 0 (
    for /d %%i in ("%USERPROFILE%\AppData\Local\Programs\Python\Python*") do (
        if exist "%%i\python.exe" (
            set PYTHON_CMD="%%i\python.exe"
            goto :found
        )
    )
    
    for /d %%i in ("%ProgramFiles%\Python*") do (
        if exist "%%i\python.exe" (
            set PYTHON_CMD="%%i\python.exe"
            goto :found
        )
    )
    
    for /d %%i in ("C:\Python*") do (
        if exist "%%i\python.exe" (
            set PYTHON_CMD="%%i\python.exe"
            goto :found
        )
    )
    
    echo [-] Python not found!
    echo Please install Python and check "Add Python to PATH".
    echo.
    pause
    exit /b
)

:found
:loop
%PYTHON_CMD% main.py
echo.
echo ====================================================
echo Bot crashed or stopped. Restarting in 5 seconds...
echo ====================================================
timeout /t 5
goto loop
