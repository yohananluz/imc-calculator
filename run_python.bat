@echo off
REM Procura Python 3 em pastas comuns e no PATH; executa o .py passado como primeiro argumento.
setlocal EnableDelayedExpansion
cd /d "%~dp0"

if "%~1"=="" (
  echo Erro: indique o script. Exemplo: run_python.bat imc_gui.py
  exit /b 1
)

set "SCRIPT=%~1"
set "FOUND="

for %%P in (
  "%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
  "%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
  "%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
  "%LOCALAPPDATA%\Programs\Python\Python310\python.exe"
) do (
  if "!FOUND!"=="" if exist %%~P (
    "%%~P" -c "import sys" 2>nul && set "FOUND=%%~P"
  )
)

if "!FOUND!"=="" (
  for %%P in (
    "%ProgramFiles%\Python312\python.exe"
    "%ProgramFiles%\Python313\python.exe"
    "%ProgramFiles%\Python311\python.exe"
    "%ProgramFiles%\Python310\python.exe"
  ) do (
    if "!FOUND!"=="" if exist %%~P (
      "%%~P" -c "import sys" 2>nul && set "FOUND=%%~P"
    )
  )
)

if not "!FOUND!"=="" (
  call :exec "!FOUND!" "!SCRIPT!"
  exit /b !errorlevel!
)

where py >nul 2>&1
if %errorlevel% equ 0 (
  py -3 -c "import sys" 2>nul
  if not errorlevel 1 (
    endlocal
    py -3 "%~1"
    exit /b %errorlevel%
  )
)

where python >nul 2>&1
if %errorlevel% equ 0 (
  python -c "import sys" 2>nul
  if not errorlevel 1 (
    endlocal
    python "%~1"
    exit /b %errorlevel%
  )
)

endlocal
echo.
echo ========================================================================
echo   Python 3 nao foi encontrado neste computador.
echo.
echo   O projeto precisa do Python instalado. Faca um dos passos abaixo:
echo.
echo   1^) Baixe em https://www.python.org/downloads/
echo      Na instalacao, MARQUE "Add python.exe to PATH".
echo.
echo   2^) Ou no PowerShell ^(Windows 10/11^):
echo        winget install Python.Python.3.12
echo.
echo   Depois instale, feche esta janela e execute o .bat de novo.
echo ========================================================================
echo.
exit /b 1

:exec
"%~1" "%~2"
exit /b %errorlevel%
