@echo off

call %~dp0bot\venv\Scripts\activate

cd %~dp0bot

set TOKEN=5836287866:AAGQ0bwUyd8L8dziVNJZjAAHvgU6-pne6qc

python bot_telegram.py

pause