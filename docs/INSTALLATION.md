# 📥 OSINT-REX Installation Guide

Complete installation instructions for all platforms.

---

## 📋 Table of Contents

- [System Requirements](#system-requirements)
- [Linux Installation](#linux-installation)
- [Windows Installation](#windows-installation)
- [MacOS Installation](#macos-installation)
- [Kali Linux Installation](#kali-linux-installation)
- [Troubleshooting](#troubleshooting)
- [Updating](#updating)

---

## 🖥️ System Requirements

### Minimum Requirements
- **Python:** 3.8 or higher
- **RAM:** 512 MB
- **Disk Space:** 50 MB
- **Internet:** Active connection required

### Recommended
- **Python:** 3.10+
- **RAM:** 1 GB+
- **Internet:** Stable broadband connection

---

## 🐧 Linux Installation

### Option 1: Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/OSINT-REX.git
cd OSINT-REX

# Install dependencies
pip3 install -r requirements.txt

# Run the tool
python3 main.py
```

### Option 2: Virtual Environment (Isolated)

```bash
# Clone repository
git clone https://github.com/yourusername/OSINT-REX.git
cd OSINT-REX

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tool
python main.py
```

### Option 3: System-Wide Installation

```bash
# Install as system package (requires sudo)
git clone https://github.com/yourusername/OSINT-REX.git
cd OSINT-REX
sudo pip3 install -r requirements.txt

# Make executable
chmod +x main.py

# Create symlink (optional)
sudo ln -s $(pwd)/main.py /usr/local/bin/osint-rex

# Run from anywhere
osint-rex
```

---

## 🪟 Windows Installation

### Prerequisites

1. **Install Python:**
   - Download from [python.org](https://www.python.org/downloads/)
   - ✅ Check "Add Python to PATH" during installation
   - Verify: `python --version`

2. **Install Git (Optional):**
   - Download from [git-scm.com](https://git-scm.com/download/win)
   - Or use GitHub Desktop

### Installation Steps

#### Method 1: Using Git

```cmd
# Open Command Prompt or PowerShell

# Clone repository
git clone https://github.com/yourusername/OSINT-REX.git
cd OSINT-REX

# Install dependencies
pip install -r requirements.txt

# Run the tool
python main.py
```

#### Method 2: Manual Download

1. Download ZIP from GitHub
2. Extract to desired location
3. Open Command Prompt in extracted folder
4. Run:
   ```cmd
   pip install -r requirements.txt
   python main.py
   ```

### Creating Desktop Shortcut (Optional)

1. Create file `OSINT-REX.bat`:
   ```batch
   @echo off
   cd C:\path\to\OSINT-REX
   python main.py
   pause
   ```
2. Right-click → Send to → Desktop

---

## 🍎 MacOS Installation

### Using Homebrew (Recommended)

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python3

# Clone repository
git clone https://github.com/yourusername/OSINT-REX.git
cd OSINT-REX

# Install dependencies
pip3 install -r requirements.txt

# Run the tool
python3 main.py
```

### Using Python.org Installer

1. Download Python from [python.org](https://www.python.org/downloads/macos/)
2. Install Python package
3. Open Terminal
4. Follow Linux instructions above

---

## 🔓 Kali Linux Installation

OSINT-REX is optimized for Kali Linux and penetration testing workflows.

### Quick Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python dependencies (usually pre-installed)
sudo apt install python3 python3-pip git -y

# Clone repository
git clone https://github.com/yourusername/OSINT-REX.git
cd OSINT-REX

# Install Python packages
pip3 install -r requirements.txt

# Run the tool
python3 main.py
```

### Adding to Kali Menu (Optional)

```bash
# Create desktop entry
sudo nano /usr/share/applications/osint-rex.desktop
```

Add content:
```ini
[Desktop Entry]
Name=OSINT-REX
Comment=Username OSINT Reconnaissance Tool
Exec=/usr/bin/python3 /path/to/OSINT-REX/main.py
Icon=/path/to/OSINT-REX/assets/icon.png
Terminal=true
Type=Application
Categories=Information Gathering;Security;
```

Save and update:
```bash
sudo update-desktop-database
```

---

## 🔧 Manual Dependency Installation

If `requirements.txt` fails, install packages individually:

```bash
pip install requests
pip install colorama
pip install tqdm
pip install pyfiglet
pip install termcolor
pip install numpy
pip install click
```

---

## 🧪 Verify Installation

Test if everything works:

```bash
# Check Python version
python3 --version  # Should be 3.8+

# Check dependencies
pip3 list | grep -E "requests|colorama|tqdm|pyfiglet"

# Run tool
python3 main.py
```

Expected output:
```
     ____  _____ _____ _   ________     ____  ________  __
    / __ \/ ___//  _/ | / /_  __/ __ \   / __ \/ ____/ |/ /
   / / / /\__ \ / //  |/ / / / / /_/ /  / /_/ / __/  |   / 
  / /_/ /___/ // // /|  / / / / _, _/  / _, _/ /___ /   |  
  \____//____/___/_/ |_/ /_/ /_/ |_|  /_/ |_/_____//_/|_|  
```

---

## 🐛 Troubleshooting

### Error: "Python not found"

**Solution:**
- Linux/Mac: Use `python3` instead of `python`
- Windows: Reinstall Python with "Add to PATH" checked

### Error: "pip: command not found"

**Solution:**
```bash
# Linux/Mac
sudo apt install python3-pip  # Debian/Ubuntu
sudo yum install python3-pip  # RedHat/CentOS

# Or use ensurepip
python3 -m ensurepip --upgrade
```

### Error: "Permission denied"

**Solution:**
```bash
# Linux/Mac - Use --user flag
pip3 install --user -r requirements.txt

# Or use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Error: "Module not found"

**Solution:**
```bash
# Reinstall dependencies
pip3 install --force-reinstall -r requirements.txt

# Or install missing module directly
pip3 install [module-name]
```

### Error: "SSL Certificate Error"

**Solution:**
```bash
# Upgrade pip and certifi
pip3 install --upgrade pip certifi

# Or disable SSL verification (not recommended)
pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Error: "sites.json not found"

**Solution:**
- Ensure `sites.json` is in the same directory as `username-checker.py`
- Check file permissions: `chmod 644 sites.json`

### Slow Performance / Timeouts

**Solution:**
1. Check internet connection
2. Some platforms may block automated requests
3. Temporarily disable firewall/antivirus
4. Use VPN if certain sites are geo-blocked

---

## 🔄 Updating OSINT-REX

### Git Update

```bash
cd OSINT-REX
git pull origin main
pip3 install --upgrade -r requirements.txt
```

### Manual Update

1. Download latest release from GitHub
2. Replace old files (keep your `sites.json` if customized)
3. Reinstall dependencies:
   ```bash
   pip3 install --upgrade -r requirements.txt
   ```

---

## 🧹 Uninstallation

### Remove OSINT-REX

```bash
# Remove directory
rm -rf OSINT-REX

# Remove Python packages (optional)
pip3 uninstall -y requests colorama tqdm pyfiglet termcolor numpy click

# Remove symlink (if created)
sudo rm /usr/local/bin/osint-rex
```

---

## 🆘 Still Having Issues?

1. **Check Python version:** `python3 --version` (must be 3.8+)
2. **Check internet connection:** `ping google.com`
3. **Read error messages carefully**
4. **Search error on Google/Stack Overflow**
5. **Open GitHub Issue** with:
   - Operating System & Version
   - Python version
   - Full error message
   - Steps to reproduce

---

## 📚 Additional Resources

- [Python Installation Guide](https://www.python.org/downloads/)
- [Pip Documentation](https://pip.pypa.io/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Git Installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

---

## ✅ Installation Complete!

You're ready to use OSINT-REX. Start with:

```bash
python3 main.py
```

Return to [README.md](README.md) for usage instructions.

---

<div align="center">

**Need help? Open an issue on GitHub!**

</div>