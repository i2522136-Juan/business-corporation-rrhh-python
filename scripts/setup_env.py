from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
VENV_DIR = BASE_DIR / ".venv"
REQUIREMENTS = BASE_DIR / "requirements.txt"


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def main() -> None:
    print("Creando entorno virtual...")
    run([sys.executable, "-m", "venv", str(VENV_DIR)])

    if os.name == "nt":
        python_bin = VENV_DIR / "Scripts" / "python.exe"
    else:
        python_bin = VENV_DIR / "bin" / "python"

    print("Actualizando pip...")
    run([str(python_bin), "-m", "pip", "install", "--upgrade", "pip"])

    print("Instalando dependencias...")
    run([str(python_bin), "-m", "pip", "install", "-r", str(REQUIREMENTS)])

    print("Entorno virtual configurado correctamente.")
    print(f"Python del entorno: {python_bin}")


if __name__ == "__main__":
    main()
