@echo off
REM Quem MANTEM o projeto: gera dist\CalculadoraIMC\ (Python precisa estar instalado so nesta maquina).
cd /d "%~dp0"
call "%~dp0run_python.bat" build.py
if errorlevel 1 pause
