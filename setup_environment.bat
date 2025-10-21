@echo off
echo ================================================
echo 🧠 Setting up Footfall Counter Environment...
echo ================================================

:: Step 1: Create virtual environment
python -m venv venv
call venv\Scripts\activate

:: Step 2: Upgrade pip
python -m pip install --upgrade pip

:: Step 3: Install dependencies
pip install -r requirements.txt

:: Step 4: Test imports
python - <<END
import cv2, torch, ultralytics, numpy
print("\n✅ All essential libraries imported successfully!")
print("Torch version:", torch.__version__)
END

echo.
echo ================================================
echo ✅ Setup Complete!
echo To activate environment later, run:
echo     venv\Scripts\activate
echo ================================================
pause
