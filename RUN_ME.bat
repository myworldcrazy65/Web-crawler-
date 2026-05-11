@echo off
color 0B
cls
echo.
echo ========================================
echo    Web Crawler EXE Builder
echo ========================================
echo.
echo Installing dependencies and building...
echo.

pip install -r requirements.txt
python build_exe.py

echo.
echo ========================================
echo    Build Complete!
echo ========================================
echo.
echo Your exe is in the 'dist' folder
echo File: dist\WebCrawler.exe
echo.
pause
