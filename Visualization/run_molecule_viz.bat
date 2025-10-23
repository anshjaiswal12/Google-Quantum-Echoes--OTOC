@echo off
echo ========================================
echo 🧬 Quantum Molecule Visualization Runner
echo 🎯 Molecular Quantum Information Spreading
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Check if required packages are installed
echo 📦 Checking required packages...
python -c "import numpy, matplotlib" >nul 2>&1
if errorlevel 1 (
    echo 📥 Installing required packages...
    echo This may take a few minutes...
    echo.
    
    REM Install packages
    pip install numpy matplotlib seaborn
    
    if errorlevel 1 (
        echo ❌ Failed to install packages
        echo Please install manually: pip install numpy matplotlib seaborn
        pause
        exit /b 1
    )
    echo ✅ Packages installed successfully
) else (
    echo ✅ All required packages are available
)

echo.
echo 🎨 Starting Molecular Visualization...
echo.

REM Run the molecular visualization
python create_molecule_viz.py

if errorlevel 1 (
    echo ❌ Error running molecular visualization
    echo Please check the script and try again
    pause
    exit /b 1
)

echo.
echo ✅ Molecular Visualization completed successfully!
echo.

REM Check for generated files
echo 📁 Generated files:
if exist "quantum_molecule_chain_reaction_*.png" echo   ✅ quantum_molecule_chain_reaction_*.png (Multi-panel visualization)
if exist "quantum_molecule_detailed_*.png" echo   ✅ quantum_molecule_detailed_*.png (Single detailed frame)

echo.
echo 🎯 Results Summary:
echo   - Multi-panel quantum information spreading visualization
echo   - Detailed single-frame molecular quantum effects
echo   - 3D molecular structure with quantum correlations
echo   - Quantum entanglement and wave effects
echo.

REM Ask if user wants to open the visualization folder
set /p choice="🔍 Would you like to open the visualization folder? (y/n): "
if /i "%choice%"=="y" (
    echo 🚀 Opening visualization folder...
    start .
) else (
    echo 📋 Visualization complete. Check the current folder for generated files.
)

echo.
echo 🎉 Thank you for exploring Quantum Molecular Visualizations!
echo 🌟 This demonstrates quantum information spreading in molecular systems
echo.
pause
