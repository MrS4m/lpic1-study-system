@echo off
title LPIC-1 Study System - Windows Launcher
color 0A
echo ================================================
echo    LPIC-1 STUDY SYSTEM - CERTIFICAÇÃO LINUX
echo ================================================
echo.
echo Inicializando aplicativo de estudo LPIC-1...
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python não encontrado!
    echo.
    echo Para instalar o Python:
    echo 1. Acesse python.org/downloads
    echo 2. Baixe Python 3.8 ou superior
    echo 3. MARQUE "Add Python to PATH" durante instalação
    echo.
    pause
    exit /b 1
)

REM Verificar se Pillow está instalado
python -c "import PIL" >nul 2>&1
if errorlevel 1 (
    echo Instalando biblioteca Pillow (requerida)...
    pip install pillow --quiet
    if errorlevel 1 (
        echo ERRO: Falha ao instalar Pillow!
        echo Tente manualmente: pip install pillow
        pause
        exit /b 1
    )
    echo Pillow instalado com sucesso!
    echo.
)

REM Verificar se arquivo principal existe
if not exist "%~dp0lpic1_app.py" (
    echo ERRO: Arquivo lpic1_app.py não encontrado!
    echo.
    echo Certifique-se que o arquivo está na mesma pasta deste .bat
    echo.
    dir *.py
    echo.
    pause
    exit /b 1
)

echo.
echo Iniciando aplicativo LPIC-1...
echo ================================================
echo.

REM Executar o aplicativo
python "%~dp0lpic1_app.py"

REM Verificar se houve erro
if errorlevel 1 (
    echo.
    echo ================================================
    echo ERRO: O aplicativo encontrou um problema.
    echo.
    echo Soluções possíveis:
    echo 1. Verifique se Python está instalado corretamente
    echo 2. Execute como Administrador
    echo 3. Tente: pip install --upgrade pillow
    echo ================================================
    echo.
)

pause