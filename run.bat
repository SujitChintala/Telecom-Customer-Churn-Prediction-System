@echo off
REM ============================================================================
REM Quick Run Script - Start the Flask Application
REM ============================================================================

echo.
echo Starting Telecom Churn Prediction Web Application...
echo.

REM Activate virtual environment
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

REM Check if model exists
if not exist "models\churn_model.pkl" (
    echo ERROR: Model not found!
    echo Please run setup.bat first or execute: python train.py
    pause
    exit /b 1
)

REM Run the Flask app
echo.
echo ================================================================================
echo Starting Flask server...
echo Application will be available at: http://localhost:5000
echo Press CTRL+C to stop the server
echo ================================================================================
echo.

python app.py
