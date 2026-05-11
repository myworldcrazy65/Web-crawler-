# 🚀 Web Crawler EXE Builder Guide

## Quick Start (Easiest Way)

### Windows Users:
1. **Double-click `RUN_ME.bat`** 
2. Wait for build to complete
3. Find your exe in `dist\WebCrawler.exe` folder ✅

### Mac/Linux Users:
```bash
python build_exe.py
```

---

## What Happens During Build?

1. ✅ Installs PyInstaller
2. ✅ Downloads NLTK data (sentence tokenizer & stopwords)
3. ✅ Downloads spaCy language model (may take 1-2 minutes first run)
4. ✅ Bundles Flask web server into exe
5. ✅ Creates `dist/WebCrawler.exe`

---

## Using Your EXE

### Option 1: From Command Line
```bash
dist\WebCrawler.exe
```

### Option 2: Double-Click
- Go to `dist` folder
- Double-click `WebCrawler.exe`
- Open your browser to: `http://127.0.0.1:5000`

### Option 3: Create Desktop Shortcut
1. Right-click `WebCrawler.exe` → Send to → Desktop (create shortcut)
2. Double-click shortcut anytime to launch

---

## Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution:** Run the build again, it will auto-install missing dependencies
```bash
python build_exe.py
```

### Issue: Port 5000 already in use
**Solution:** The app will try port 5001, 5002, etc. automatically

### Issue: First run is slow
**Solution:** Normal! spaCy model is being loaded. Subsequent runs are fast.

### Issue: Antivirus warning
**Solution:** This is normal for packaged exe files. Add to exceptions or use the Flask version instead.

---

## Distributing Your EXE

You can share just the `WebCrawler.exe` file with others! They can:
- Copy it anywhere
- Double-click to run
- No Python installation needed

---

## Advanced: Building Without Debug Mode

The build script automatically disables debug mode in the exe for better performance.

---

## Size Info

- **Executable size:** ~150-200MB (includes Python runtime + all libraries)
- **First run:** Downloads language models (~50MB)
- **Subsequent runs:** Fast! (~3-5 seconds to load)

---

## Need Help?

If build fails:
1. Make sure Python 3.8+ is installed
2. Update pip: `python -m pip install --upgrade pip`
3. Delete `build`, `dist`, and `.spec` folders
4. Run build again: `python build_exe.py`

Enjoy! 🎉
