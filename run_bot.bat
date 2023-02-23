@echo off

call %~dp0\venv\Scripts\activate

cd %~dp0project

set TOKEN=6263683643:AAGdvFkayZrYREiZagK2BQAcnZQyjUPgcYw

python main.py

pause