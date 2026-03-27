@echo off
cd /d "%~dp0"
call "%~dp0run_python.bat" imc_gui.py
if errorlevel 1 pause
