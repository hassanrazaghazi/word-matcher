@echo off

:: Step 1: Check if a virtual environment exists, if not, create one
IF NOT EXIST "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Step 2: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Step 3: Install required packages from requirements.txt
echo Installing required packages...
pip install -r requirements.txt

:: Step 4: Deactivate the virtual environment
:: echo Deactivating virtual environment...
:: deactivate

:: echo Virtual environment setup complete.
pause
