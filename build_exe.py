import PyInstaller.__main__
import os
import sys
import shutil

print("=" * 50)
print("Web Crawler EXE Builder")
print("=" * 50)

# Clean previous builds
print("\n[1/4] Cleaning previous builds...")
for folder in ['build', 'dist', '__pycache__']:
    if os.path.exists(folder):
        shutil.rmtree(folder)
        print(f"  ✓ Removed {folder}")

# Install PyInstaller if needed
print("\n[2/4] Ensuring PyInstaller is installed...")
try:
    import PyInstaller
    print("  ✓ PyInstaller ready")
except ImportError:
    print("  Installing PyInstaller...")
    os.system(f"{sys.executable} -m pip install pyinstaller")

# Build the exe
print("\n[3/4] Building executable...")
PyInstaller.__main__.run([
    'app.py',
    '--name=WebCrawler',
    '--onefile',
    '--windowed',
    '--add-data=templates:templates',
    '--hidden-import=nltk',
    '--hidden-import=spacy',
    '--hidden-import=duckduckgo_search',
    '--icon=NONE',
    '--distpath=dist',
    '--buildpath=build',
    '--specpath=.'
])

# Success message
print("\n[4/4] Complete!")
print("=" * 50)
print("✓ Build successful!")
print("=" * 50)
print("\nYour exe is ready:")
print(f"  📁 Location: dist\\WebCrawler.exe")
print(f"\nTo run:")
print(f"  1. Double-click: dist\\WebCrawler.exe")
print(f"  2. Or command line: dist\\WebCrawler.exe")
print(f"\nYour app will open at: http://127.0.0.1:5000")
print("=" * 50)
