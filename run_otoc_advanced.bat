@echo off
setlocal enabledelayedexpansion

echo ========================================
echo 🚀 Advanced Quantum OTOC Launcher
echo 🎯 Google's Quantum Advantage Recreation
echo ========================================
echo.

REM Set colors for better output
color 0A

REM Check if Python is installed
echo 🔍 Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo.
    echo 📥 Please install Python 3.7+ from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python !PYTHON_VERSION! found

REM Check if we're in the right directory
if not exist "OTOC.ipynb" (
    echo ❌ OTOC.ipynb not found in current directory
    echo Please run this script from the directory containing OTOC.ipynb
    pause
    exit /b 1
)

echo ✅ OTOC.ipynb found
echo.

REM Create virtual environment if it doesn't exist
if not exist "otoc_env" (
    echo 📦 Creating virtual environment...
    python -m venv otoc_env
    if errorlevel 1 (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )
    echo ✅ Virtual environment created
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call otoc_env\Scripts\activate.bat

REM Check if required packages are installed
echo 📦 Checking required packages...
python -c "import cirq, numpy, matplotlib, seaborn, jupyter" >nul 2>&1
if errorlevel 1 (
    echo 📥 Installing required packages...
    echo This may take a few minutes...
    echo.
    
    REM Install packages with specific versions for compatibility
    pip install --upgrade pip
    pip install cirq==1.2.0 numpy matplotlib seaborn jupyter ipykernel notebook
    
    if errorlevel 1 (
        echo ❌ Failed to install packages
        echo.
        echo 🔧 Troubleshooting:
        echo 1. Check your internet connection
        echo 2. Try running: pip install --upgrade pip
        echo 3. Try running: pip install cirq numpy matplotlib seaborn jupyter
        echo.
        pause
        exit /b 1
    )
    echo ✅ Packages installed successfully
) else (
    echo ✅ All required packages are available
)

echo.
echo 🎨 Starting OTOC Demonstration...
echo.

REM Create a backup of the original notebook
if not exist "OTOC_backup.ipynb" (
    echo 💾 Creating backup of original notebook...
    copy "OTOC.ipynb" "OTOC_backup.ipynb" >nul
    echo ✅ Backup created as OTOC_backup.ipynb
)

REM Run the notebook with progress tracking
echo 📊 Executing OTOC.ipynb...
echo This will run all cells and generate visualizations...
echo.

REM Use nbconvert to execute the notebook
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 OTOC.ipynb

if errorlevel 1 (
    echo ❌ Error executing notebook
    echo.
    echo 🔧 Troubleshooting:
    echo 1. Check if all cells in the notebook are valid
    echo 2. Ensure you have enough memory (OTOC simulation can be memory-intensive)
    echo 3. Try running individual cells manually in Jupyter
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ OTOC Demonstration completed successfully!
echo.

REM Check for generated files
echo 📁 Generated files:
if exist "Output\otoc_circuit_structure_*.png" echo   ✅ Output/otoc_circuit_structure_*.png (Circuit diagram)
if exist "Output\otoc_vs_depth_*.png" echo   ✅ Output/otoc_vs_depth_*.png (Scrambling analysis)
if exist "Output\quantum_vs_classical_*.png" echo   ✅ Output/quantum_vs_classical_*.png (Complexity comparison)
if exist "Output\quantum_echoes_*.png" echo   ✅ Output/quantum_echoes_*.png (Interference effects)
if exist "Output\otoc_summary_*.txt" echo   ✅ Output/otoc_summary_*.txt (Summary report)
if exist "OTOC.ipynb" echo   ✅ OTOC.ipynb (executed notebook with outputs)
echo   ✅ OTOC_backup.ipynb (original notebook backup)

echo.
echo 🎯 Results Summary:
echo   - Quantum circuit construction and simulation completed
echo   - Information scrambling analysis performed
echo   - Quantum vs classical complexity comparison generated
echo   - All visualizations and plots created
echo.

REM Ask user what they want to do next
echo 🔍 What would you like to do next?
echo.
echo 1. Open the executed notebook in Jupyter
echo 2. Open the executed notebook in your default browser
echo 3. View the generated plots in Output folder
echo 4. Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo 🚀 Opening notebook in Jupyter...
    jupyter notebook OTOC.ipynb
) else if "%choice%"=="2" (
    echo 🌐 Opening notebook in browser...
    start OTOC.ipynb
) else if "%choice%"=="3" (
    echo 🖼️ Opening Output folder with generated plots...
    start Output
    echo 📖 Open individual PNG files to view visualizations
) else (
    echo 📋 Notebook execution complete. You can open OTOC.ipynb manually.
)

echo.
echo 🎉 Thank you for exploring Quantum OTOC!
echo 🌟 This demonstrates Google's quantum supremacy achievement
echo.
echo 📚 Learn more about:
echo   - Google's 2019 quantum supremacy paper
echo   - Cirq quantum computing framework
echo   - Quantum information theory
echo.

REM Deactivate virtual environment
call otoc_env\Scripts\deactivate.bat

pause
