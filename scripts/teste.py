import sys
print("Python version:", sys.version)
print("\nChecking dependencies...")

try:
    import tkinter
    print("✓ tkinter OK")
except ImportError as e:
    print("✗ tkinter ERROR:", e)

try:
    from PIL import Image, ImageTk
    print("✓ Pillow OK")
except ImportError as e:
    print("✗ Pillow ERROR:", e)

print("\nSystem PATH:")
for path in sys.path[:10]:
    print(" ", path)

input("\nPress Enter to exit...")