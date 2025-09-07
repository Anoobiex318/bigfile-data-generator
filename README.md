# Datagen – Test Data File Generator

Datagen is a lightweight Python tool for generating **large test data files** in either **CSV** or **SQL** format.  
It is designed for **Data Engineering ETL projects**, where realistic, large-scale datasets are needed for testing pipelines and performance.

---

## ✨ Features
- Generate files of any size (in **GB**).
- Choose output format:
  - **CSV** (comma-separated values)
  - **SQL** (INSERT statements)
- Automatic filename formatting:
<size>gb_testdata<timestamp>-<rowcount>.csv

- Real-time progress display while generating.
- Cross-platform support (Windows, Linux, macOS).

---

## 🚀 Usage

Run the tool:

```bash
python datagen.py


🛠️ Build Instructions
🔹 Windows (EXE build)

Install Python
 (3.9+ recommended).

Install PyInstaller

pip install pyinstaller
pyinstaller --onefile --console datagen.py --icon=icon.ico
