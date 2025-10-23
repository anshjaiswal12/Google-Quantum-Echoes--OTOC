#!/usr/bin/env python3
"""
Quantum OTOC Demonstration Runner
Automatically executes the OTOC.ipynb notebook with all visualizations
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_banner():
    """Print a beautiful banner"""
    print("=" * 60)
    print("🚀 Quantum OTOC Demonstration Runner")
    print("🎯 Google's Quantum Advantage Recreation")
    print("=" * 60)
    print()

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7+ is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def check_notebook_exists():
    """Check if OTOC.ipynb exists"""
    if not Path("OTOC.ipynb").exists():
        print("❌ OTOC.ipynb not found in current directory")
        print("Please run this script from the directory containing OTOC.ipynb")
        return False
    print("✅ OTOC.ipynb found")
    return True

def install_packages():
    """Install required packages"""
    packages = [
        "cirq>=1.2.0",
        "numpy",
        "matplotlib",
        "seaborn",
        "jupyter",
        "ipykernel",
        "nbconvert"
    ]
    
    print("📦 Installing required packages...")
    print("This may take a few minutes...")
    print()
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", package, "--upgrade"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"✅ {package} installed")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
            return False
    
    return True

def check_packages():
    """Check if required packages are installed"""
    required_packages = ["cirq", "numpy", "matplotlib", "seaborn", "jupyter"]
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"❌ {package} not found")
            return False
    
    print("✅ All required packages are available")
    return True

def execute_notebook():
    """Execute the OTOC notebook"""
    print("📊 Executing OTOC.ipynb...")
    print("This will run all cells and generate visualizations...")
    print()
    
    try:
        # Use nbconvert to execute the notebook
        result = subprocess.run([
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--inplace",
            "--ExecutePreprocessor.timeout=300",
            "OTOC.ipynb"
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print("❌ Error executing notebook:")
            print(result.stderr)
            return False
        
        print("✅ OTOC notebook executed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def create_backup():
    """Create backup of original notebook"""
    if not Path("OTOC_backup.ipynb").exists():
        try:
            import shutil
            shutil.copy2("OTOC.ipynb", "OTOC_backup.ipynb")
            print("💾 Backup created as OTOC_backup.ipynb")
        except Exception as e:
            print(f"⚠️ Could not create backup: {e}")

def show_results():
    """Show execution results"""
    print()
    print("📁 Generated files:")
    
    # Check Output directory
    output_dir = Path("Output")
    if output_dir.exists():
        output_files = list(output_dir.glob("*.png"))
        if output_files:
            print(f"  ✅ Output/ directory with {len(output_files)} visualizations:")
            for file_path in output_files:
                print(f"    • {file_path.name}")
    
    files_to_check = [
        ("OTOC.ipynb", "executed notebook with outputs"),
        ("OTOC_backup.ipynb", "original notebook backup")
    ]
    
    for filename, description in files_to_check:
        if Path(filename).exists():
            print(f"  ✅ {filename} ({description})")
    
    print()
    print("🎯 Results Summary:")
    print("  - Quantum circuit construction and simulation completed")
    print("  - Information scrambling analysis performed")
    print("  - Quantum vs classical complexity comparison generated")
    print("  - All visualizations saved to Output/ directory")
    print()

def open_notebook():
    """Ask user if they want to open the notebook"""
    print("🔍 What would you like to do next?")
    print()
    print("1. Open the executed notebook in Jupyter")
    print("2. Open the executed notebook in your default browser")
    print("3. View the generated plots")
    print("4. Exit")
    print()
    
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            print("🚀 Opening notebook in Jupyter...")
            try:
                subprocess.run([sys.executable, "-m", "jupyter", "notebook", "OTOC.ipynb"])
            except Exception as e:
                print(f"❌ Error opening Jupyter: {e}")
            break
        elif choice == "2":
            print("🌐 Opening notebook in browser...")
            try:
                if platform.system() == "Windows":
                    os.startfile("OTOC.ipynb")
                elif platform.system() == "Darwin":  # macOS
                    subprocess.run(["open", "OTOC.ipynb"])
                else:  # Linux
                    subprocess.run(["xdg-open", "OTOC.ipynb"])
            except Exception as e:
                print(f"❌ Error opening notebook: {e}")
            break
        elif choice == "3":
            print("🖼️ Opening Output folder with generated plots...")
            output_dir = Path("Output")
            if output_dir.exists():
                try:
                    if platform.system() == "Windows":
                        os.startfile(str(output_dir))
                    elif platform.system() == "Darwin":
                        subprocess.run(["open", str(output_dir)])
                    else:
                        subprocess.run(["xdg-open", str(output_dir)])
                except Exception as e:
                    print(f"❌ Error opening Output folder: {e}")
            else:
                print("❌ Output folder not found")
            print("📖 Open individual PNG files to view visualizations")
            break
        elif choice == "4":
            print("📋 Notebook execution complete. You can open OTOC.ipynb manually.")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

def main():
    """Main function"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Check if notebook exists
    if not check_notebook_exists():
        return 1
    
    # Create backup
    create_backup()
    
    # Check packages
    if not check_packages():
        print("📥 Installing missing packages...")
        if not install_packages():
            print("❌ Failed to install required packages")
            return 1
    
    # Execute notebook
    if not execute_notebook():
        print("❌ Failed to execute notebook")
        return 1
    
    # Show results
    show_results()
    
    # Ask user what to do next
    open_notebook()
    
    print()
    print("🎉 Thank you for exploring Quantum OTOC!")
    print("🌟 This demonstrates Google's quantum supremacy achievement")
    print()
    print("📚 Learn more about:")
    print("  - Google's 2019 quantum supremacy paper")
    print("  - Cirq quantum computing framework")
    print("  - Quantum information theory")
    print()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
