@echo off

:: Step 1: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Step 2: Run the Python file
echo Running the application...
streamlit run "Dynamic Word Matcher.py"

:: Step 3: Deactivate the virtual environment after running the script
:: echo Deactivating virtual environment...
:: deactivate

pause
