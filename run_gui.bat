@echo off
cd /d "%~dp0"
"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" imc_gui.py
if errorlevel 1 (
  echo.
  echo Se deu erro, confira se o Python esta em Python312 ou ajuste este .bat
  pause
)
