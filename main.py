# main.py
import os
import sys

if __name__ == "__main__":
    try:
        # username-checker.py dosyasını çalıştır
        os.system(f"{sys.executable} username-checker.py")
    except KeyboardInterrupt:
        print("\nStopped by User")
        sys.exit(0)
