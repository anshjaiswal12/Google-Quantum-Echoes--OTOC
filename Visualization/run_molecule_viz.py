#!/usr/bin/env python3
"""
Quantum Molecule Visualization Runner
Cross-platform script to run molecular quantum visualizations
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_banner():
    """Print a beautiful banner"""
    print("=" * 60)
    print("Quantum Molecule Visualization Runner")
    print("Molecular Quantum Information Spreading")
    print("=" * 60)
    print()

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("ERROR: Python 3.7+ is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"SUCCESS: Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def check_script_exists():
    """Check if the visualization script exists"""
    if not Path("create_molecule_viz.py").exists():
        print("ERROR: create_molecule_viz.py not found in current directory")
        print("Please run this script from the Visualization directory")
        return False
    print("SUCCESS: Molecular visualization script found")
    return True

def install_packages():
    """Install required packages"""
    packages = [
        "numpy",
        "matplotlib",
        "seaborn"
    ]
    
    print("Installing required packages...")
    print("This may take a few minutes...")
    print()
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", package, "--upgrade"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"SUCCESS: {package} installed")
        except subprocess.CalledProcessError:
            print(f"ERROR: Failed to install {package}")
            return False
    
    return True

def check_packages():
    """Check if required packages are installed"""
    required_packages = ["numpy", "matplotlib", "seaborn"]
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"ERROR: {package} not found")
            return False
    
    print("SUCCESS: All required packages are available")
    return True

def run_visualization():
    """Run the molecular visualization script"""
    print("Starting Molecular Visualization...")
    print()
    
    try:
        # Import and run the visualization
        import create_molecule_viz
        create_molecule_viz.main()
        return True
    except Exception as e:
        print(f"ERROR: Error running visualization: {e}")
        return False

def show_results():
    """Show execution results"""
    print()
    print("Generated files:")
    
    # Check for generated files
    files_to_check = [
        ("quantum_molecule_chain_reaction_*.png", "Multi-panel chain reaction visualization"),
        ("quantum_molecule_detailed_*.png", "Detailed single-frame visualization")
    ]
    
    for pattern, description in files_to_check:
        matching_files = list(Path(".").glob(pattern))
        if matching_files:
            print(f"  SUCCESS: {len(matching_files)} {description} file(s)")
            for file_path in matching_files:
                print(f"    - {file_path.name}")
    
    print()
    print("Results Summary:")
    print("  - Multi-panel quantum information spreading visualization")
    print("  - Detailed single-frame molecular quantum effects")
    print("  - 3D molecular structure with quantum correlations")
    print("  - Quantum entanglement and wave effects")
    print()

def open_visualization():
    """Ask user if they want to open the visualization folder"""
    print("What would you like to do next?")
    print()
    print("1. Open the visualization folder")
    print("2. View the generated images")
    print("3. Run the visualization again")
    print("4. Exit")
    print()
    
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            print("Opening visualization folder...")
            try:
                if platform.system() == "Windows":
                    os.startfile(".")
                elif platform.system() == "Darwin":  # macOS
                    subprocess.run(["open", "."])
                else:  # Linux
                    subprocess.run(["xdg-open", "."])
            except Exception as e:
                print(f"ERROR: Error opening folder: {e}")
            break
        elif choice == "2":
            print("Opening generated visualizations...")
            try:
                for file_path in Path(".").glob("quantum_molecule_*.png"):
                    if platform.system() == "Windows":
                        os.startfile(str(file_path))
                    elif platform.system() == "Darwin":
                        subprocess.run(["open", str(file_path)])
                    else:
                        subprocess.run(["xdg-open", str(file_path)])
            except Exception as e:
                print(f"ERROR: Error opening images: {e}")
            break
        elif choice == "3":
            print("Running visualization again...")
            if run_visualization():
                show_results()
            break
        elif choice == "4":
            print("Visualization complete. Check the current folder for generated files.")
            break
        else:
            print("ERROR: Invalid choice. Please enter 1, 2, 3, or 4.")

def main():
    """Main function"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Check if script exists
    if not check_script_exists():
        return 1
    
    # Check packages
    if not check_packages():
        print("Installing missing packages...")
        if not install_packages():
            print("ERROR: Failed to install required packages")
            return 1
    
    # Run visualization
    if not run_visualization():
        print("ERROR: Failed to run visualization")
        return 1
    
    # Show results
    show_results()
    
    # Ask user what to do next
    open_visualization()
    
    print()
    print("Thank you for exploring Quantum Molecular Visualizations!")
    print("This demonstrates quantum information spreading in molecular systems")
    print()
    print("Learn more about:")
    print("  - Quantum information theory")
    print("  - Molecular quantum mechanics")
    print("  - Quantum entanglement in chemistry")
    print()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
