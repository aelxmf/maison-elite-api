@echo off
REM ==========================================
REM  Lance l'API Maison Élite et ouvre /docs
REM  automatiquement dans le navigateur.
REM
REM  Double-cliquez simplement sur ce fichier
REM  pour tout démarrer d'un coup.
REM ==========================================

REM Se place dans le dossier où se trouve ce fichier .bat
cd /d "%~dp0"

REM Ouvre la page /docs dans le navigateur par défaut
REM (avec un petit délai pour laisser le serveur démarrer)
start "" cmd /c "timeout /t 2 >nul && start http://127.0.0.1:8000/docs"

REM Lance le serveur (cette fenêtre doit rester ouverte)
uvicorn main:app --reload

pause
