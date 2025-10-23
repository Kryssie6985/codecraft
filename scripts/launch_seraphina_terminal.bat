@echo off
title SERAPHINA Federation Terminal
echo 🌌 Launching SERAPHINA Federation Terminal...

REM Set UTF-8 code page for Unicode support
chcp 65001 > nul

REM Set environment variables for Python UTF-8 support
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1

REM Launch the SERAPHINA Terminal
python seraphina_terminal.py

pause