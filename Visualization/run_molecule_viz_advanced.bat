@echo off
setlocal enabledelayedexpansion

echo ========================================
echo 🧬 Advanced Quantum Molecule Visualizer
echo 🎯 Molecular Quantum Information Spreading
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
if not exist "create_molecule_viz.py" (
    echo ❌ create_molecule_viz.py not found in current directory
    echo Please run this script from the Visualization directory
    pause
    exit /b 1
)

echo ✅ Molecular visualization script found
echo.

REM Create virtual environment if it doesn't exist
if not exist "molecule_env" (
    echo 📦 Creating virtual environment for molecular visualization...
    python -m venv molecule_env
    if errorlevel 1 (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )
    echo ✅ Virtual environment created
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call molecule_env\Scripts\activate.bat

REM Check if required packages are installed
echo 📦 Checking required packages...
python -c "import numpy, matplotlib, seaborn" >nul 2>&1
if errorlevel 1 (
    echo 📥 Installing required packages...
    echo This may take a few minutes...
    echo.
    
    REM Install packages with specific versions for compatibility
    pip install --upgrade pip
    pip install numpy matplotlib seaborn mpl_toolkits
    
    if errorlevel 1 (
        echo ❌ Failed to install packages
        echo.
        echo 🔧 Troubleshooting:
        echo 1. Check your internet connection
        echo 2. Try running: pip install --upgrade pip
        echo 3. Try running: pip install numpy matplotlib seaborn
        echo.
        pause
        exit /b 1
    )
    echo ✅ Packages installed successfully
) else (
    echo ✅ All required packages are available
)

echo.
echo 🎨 Starting Advanced Molecular Visualization...
echo.

REM Create a backup of the original script
if not exist "create_molecule_viz_backup.py" (
    echo 💾 Creating backup of original script...
    copy "create_molecule_viz.py" "create_molecule_viz_backup.py" >nul
    echo ✅ Backup created as create_molecule_viz_backup.py
)

REM Run the molecular visualization
python create_molecule_viz.py

if errorlevel 1 (
    echo ❌ Error running molecular visualization
    echo.
    echo 🔧 Troubleshooting:
    echo 1. Check if all required packages are installed
    echo 2. Ensure you have enough memory (visualization can be memory-intensive)
    echo 3. Try running the script manually: python create_molecule_viz.py
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ Advanced Molecular Visualization completed successfully!
echo.

REM Check for generated files
echo 📁 Generated files:
if exist "quantum_molecule_chain_reaction_*.png" echo   ✅ quantum_molecule_chain_reaction_*.png (Multi-panel chain reaction)
if exist "quantum_molecule_detailed_*.png" echo   ✅ quantum_molecule_detailed_*.png (Detailed single frame)
if exist "create_molecule_viz_backup.py" echo   ✅ create_molecule_viz_backup.py (Script backup)

echo.
echo 🎯 Results Summary:
echo   - Multi-panel quantum information spreading visualization
echo   - Detailed single-frame molecular quantum effects
echo   - 3D molecular structure with quantum correlations
echo   - Quantum entanglement and wave effects
echo   - Scientific publication-ready visualizations
echo.

REM Ask user what they want to do next
echo 🔍 What would you like to do next?
echo.
echo 1. Open the visualization folder
echo 2. View the generated images
echo 3. Run the visualization again
echo 4. Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo 🚀 Opening visualization folder...
    start .
) else if "%choice%"=="2" (
    echo 🖼️ Opening generated visualizations...
    for %%f in (quantum_molecule_*.png) do start "" "%%f"
) else if "%choice%"=="3" (
    echo 🔄 Running visualization again...
    python create_molecule_viz.py
) else (
    echo 📋 Visualization complete. Check the current folder for generated files.
)

echo.
echo 🎉 Thank you for exploring Quantum Molecular Visualizations!
echo 🌟 This demonstrates quantum information spreading in molecular systems
echo.
echo 📚 Learn more about:
echo   - Quantum information theory
echo   - Molecular quantum mechanics
echo   - Quantum entanglement in chemistry
echo.

REM Deactivate virtual environment
call molecule_env\Scripts\deactivate.bat

pause
