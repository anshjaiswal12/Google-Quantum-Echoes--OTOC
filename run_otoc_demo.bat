@echo off
echo ========================================
echo 🚀 Quantum OTOC Demonstration Launcher
echo 🎯 Google's Quantum Advantage Recreation
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
python -c "import cirq, numpy, matplotlib, seaborn" >nul 2>&1
if errorlevel 1 (
    echo 📥 Installing required packages...
    echo This may take a few minutes...
    echo.
    
    REM Install packages
    pip install cirq numpy matplotlib seaborn jupyter ipykernel
    
    if errorlevel 1 (
        echo ❌ Failed to install packages
        echo Please install manually: pip install cirq numpy matplotlib seaborn jupyter
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

REM Run the notebook
echo 📊 Executing OTOC.ipynb...
jupyter nbconvert --to notebook --execute --inplace OTOC.ipynb

if errorlevel 1 (
    echo ❌ Error executing notebook
    echo Please check the notebook file and try again
    pause
    exit /b 1
)

echo.
echo ✅ OTOC Demonstration completed successfully!
echo.
echo 📁 Generated files:
echo   - OTOC.ipynb (executed notebook with outputs)
echo   - Output/ directory with all visualizations
echo     * otoc_circuit_structure_*.png
echo     * otoc_vs_depth_*.png  
echo     * quantum_vs_classical_*.png
echo     * quantum_echoes_*.png
echo     * otoc_summary_*.txt
echo.
echo 🎯 The notebook has been executed with all visualizations and analysis
echo 📖 Open OTOC.ipynb to view the results
echo 📁 Check the Output/ folder for all generated plots
echo.

REM Ask if user wants to open the notebook
set /p choice="🔍 Would you like to open the notebook in Jupyter? (y/n): "
if /i "%choice%"=="y" (
    echo 🚀 Opening notebook in Jupyter...
    jupyter notebook OTOC.ipynb
) else (
    echo 📋 Notebook execution complete. You can open OTOC.ipynb manually.
)

echo.
echo 🎉 Thank you for exploring Quantum OTOC!
echo 🌟 This demonstrates Google's quantum supremacy achievement
echo.
pause
