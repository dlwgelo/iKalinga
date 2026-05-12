"""Buildozer entrypoint for the Kivy frontend."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
APP_DIR = ROOT / "kivy_app"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from kivy_app.main import iKalingaApp


if __name__ == "__main__":
    app = iKalingaApp()
    app.title = "iKalinga - Appointment System"
    app.run()