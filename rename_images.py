import os
from pathlib import Path

# Rename images in original folder
original_dir = Path.home() / "Desktop" / "Gameshow" / "images" / "original"
files = sorted([f for f in original_dir.glob("*.png")])
for i, file in enumerate(files, start=1):
    new_name = f"{i}.png"
    file.rename(original_dir / new_name)
    print(f"Renamed {file.name} -> {new_name}")

# Rename images in altered folder
altered_dir = Path.home() / "Desktop" / "Gameshow" / "images" / "altered"
files = sorted([f for f in altered_dir.glob("*.png")])
for i, file in enumerate(files, start=1):
    new_name = f"{i}.png"
    file.rename(altered_dir / new_name)
    print(f"Renamed {file.name} -> {new_name}")

print("\nAll images renamed successfully!")
