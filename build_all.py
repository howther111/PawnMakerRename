import os
import subprocess

for file in os.listdir():
    if file.endswith(".py"):
        subprocess.run(["pyinstaller", "--onefile", file])