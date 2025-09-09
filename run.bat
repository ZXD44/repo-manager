@echo off
chcp 65001 >nul 2>&1
title 🚀 GitHub Repository Manager - ZirconX
color 0A

echo.
echo ╔══════════════════════════════════════════════════════════════════════════════╗
echo ║                    🚀 GitHub Repository ^& Release Manager                   ║
echo ║                        ⚡ Quick Start Launcher v1.1.0                       ║
echo ║                                                                              ║
echo ║                          👨‍💻 Developed by ZirconX                            ║
echo ╚══════════════════════════════════════════════════════════════════════════════╝
echo.

REM Check Python
echo 🔍 Checking system requirements...
echo.
echo [1/3] Python Environment Check...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found!
    echo.
    echo 💡 Please install Python 3.x from:
    echo    https://python.org/downloads
    echo.
    echo ⚠️  Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
) else (
    for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
    echo ✅ %PYTHON_VERSION% - Ready
)

echo.
echo [2/3] Dependencies Check...
python -c "import requests" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Installing required package: requests
    python -m pip install requests
    if errorlevel 1 (
        echo ❌ Failed to install requests
        echo 💡 Please run: pip install requests
        pause
        exit /b 1
    )
    echo ✅ requests - Installed
) else (
    echo ✅ requests - Available
)

echo.
echo [3/3] Starting application...
echo ╭─────────────────────────────────────────────────────────────╮
echo │                  🎯 Launching GitHub Manager                │
echo ╰─────────────────────────────────────────────────────────────╯
echo.

REM Run program
python repo_manager.py

REM Check exit code
if errorlevel 1 (
    echo.
    echo ╭─────────────────────────────────────────────────────────────╮
    echo │                    ❌ Program Error Detected                │
    echo ╰─────────────────────────────────────────────────────────────╯
    echo.
    echo 💡 Troubleshooting tips:
    echo    • Check your Python installation
    echo    • Make sure all files are in the same folder
    echo    • Check QUICK_FIX.txt for GitHub Token issues
    echo.
) else (
    echo.
    echo ╭─────────────────────────────────────────────────────────────╮
    echo │              🎉 Thanks for using GitHub Manager!           │
    echo ╰─────────────────────────────────────────────────────────────╯
    echo.
)

echo Press any key to exit...
pause >nul