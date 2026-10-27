@echo off
title Walmart Sales Intelligence Studio Launcher
cls
echo ====================================================================
echo    WALMART STORE SALES FORECASTING & ECONOMETRICS STUDIO
echo    RVCE Applied Data Science Skill Lab — Mini-Project Demo
echo ====================================================================
echo.
echo Choose your presentation environment:
echo.
echo [1] Launch Standalone Executive Web UI (Fastest, zero install, runs offline)
echo [2] Launch Python Streamlit Interactive Dashboard
echo [3] Launch Python REST Server (http://localhost:8000)
echo [4] Open Viva Presentation Guide in Notepad
echo [5] Exit
echo.
set /p choice="Enter option (1, 2, 3, 4, 5): "

if "%choice%"=="1" (
    echo.
    echo Launching Standalone Executive Web UI in default browser...
    start "" "%~dp0index.html"
    exit /b
)

if "%choice%"=="2" (
    echo.
    echo Starting Streamlit App on http://localhost:8501...
    streamlit run app.py
    pause
    exit /b
)

if "%choice%"=="3" (
    echo.
    echo Starting Python Server on http://localhost:8000...
    start "" http://localhost:8000
    python server.py
    pause
    exit /b
)

if "%choice%"=="4" (
    echo.
    echo Opening Viva Defense Guide...
    notepad "%~dp0VIVA_PREPARATION_GUIDE.md"
    exit /b
)

if "%choice%"=="5" (
    exit /b
)

echo Invalid choice.
pause
