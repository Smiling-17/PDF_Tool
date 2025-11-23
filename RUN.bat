@echo off
title PDF Master Tool Launcher
echo Dang khoi dong PDF Master Tool...
echo -------------------------------------------------

:: Kiem tra xem da cai thu vien chua, neu chua thi tu cai
python -c "import pypdf" 2>NUL
if %errorlevel% neq 0 (
    echo Phat hien thieu thu vien. Dang tu dong cai dat...
    pip install pypdf
)

:: Chay tool bang pythonw (khong hien cua so den)
start "" pythonw main.py

exit
