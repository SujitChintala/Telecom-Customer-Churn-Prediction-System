@echo off
REM ============================================================================
REM Telecom Churn Prediction - Windows Setup Script
REM ============================================================================

echo.
echo ================================================================================
echo TELECOM CUSTOMER CHURN PREDICTION - AUTOMATED SETUP
echo ================================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Python detected...
python --version

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    echo.
    echo [2/5] Creating virtual environment...
    python -m venv .venv
    echo Virtual environment created successfully!
) else (
    echo.
    echo [2/5] Virtual environment already exists, skipping...
)

REM Activate virtual environment and install dependencies
echo.
echo [3/5] Activating virtual environment and installing dependencies...
call .venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt

REM Check if model exists
if not exist "models\churn_model.pkl" (
    echo.
    echo [4/5] Model not found. Training model...
    python train.py
) else (
    echo.
    echo [4/5] Model already exists, skipping training...
    echo To retrain the model, delete the models folder and run this script again.
)

REM Done
echo.
echo [5/5] Setup complete!
echo.
echo ================================================================================
echo SETUP COMPLETED SUCCESSFULLY!
echo ================================================================================
echo.
echo You can now:
echo   1. Run the web application: python app.py
echo   2. Open Jupyter notebook for EDA: jupyter notebook notebooks/01_EDA_and_Analysis.ipynb
echo   3. Retrain the model: python train.py
echo.
echo The web application will be available at: http://localhost:5000
echo.
echo Press any key to exit...
pause >nul
