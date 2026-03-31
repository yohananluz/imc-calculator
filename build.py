"""Gera o executavel Windows com PyInstaller (quem desenvolve roda isto; quem recebe o .exe nao precisa de Python)."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", str(ROOT / "requirements-build.txt")]
    )
    try:
        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "PyInstaller",
                "--noconfirm",
                "--clean",
                str(ROOT / "CalculadoraIMC.spec"),
            ]
        )
    except subprocess.CalledProcessError:
        print(
            "\nSe houve erro de permissão ao apagar dist\\CalculadoraIMC: "
            "feche o CalculadoraIMC.exe se estiver aberto, "
            "pause a sincronização do OneDrive nesta pasta ou apague dist\\CalculadoraIMC manualmente e rode de novo."
        )
        raise
    exe = ROOT / "dist" / "CalculadoraIMC" / "CalculadoraIMC.exe"
    print(f"\nPronto. Executavel: {exe}")
    print("Distribua a pasta inteira dist\\CalculadoraIMC\\ (ou compacte em ZIP).")


if __name__ == "__main__":
    main()
