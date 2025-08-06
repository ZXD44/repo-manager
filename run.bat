@echo off
chcp 65001 >nul 2>&1
title Repository Manager

echo.
echo ==========================================
echo Repository ^& Release Manager
echo ==========================================
echo.

REM Check Python
echo Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found
    echo Please install Python from https://python.org
    echo and add Python to PATH
    echo.
    pause
    exit /b 1
) else (
    python --version
    echo Python ready
)

echo.
echo Starting program...
echo.

REM Run program
python repo_manager.py

if errorlevel 1 (
    echo.
    echo Error running program
    echo.
)

pause