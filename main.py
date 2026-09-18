"""
AI-Powered Sustainable Predictive Maintenance System
-----------------------------------------------------
Entry point — run this file to launch the Streamlit app.

Usage:
    python main.py
"""

import subprocess
import sys
from pathlib import Path


def main():
    app_path = Path(__file__).resolve().parent / "app" / "app.py"

    if not app_path.exists():
        print(f"[ERROR] app.py not found at: {app_path}")
        sys.exit(1)

    print("🌱 Starting AI Sustainable Predictive Maintenance System...")
    print(f"   App  : {app_path}")
    print("   URL  : http://localhost:8501")
    print("   Press Ctrl+C to stop.\n")

    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", str(app_path)],
        check=True,
    )


if __name__ == "__main__":
    main()
