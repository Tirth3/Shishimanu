## 🐾 Shishimanu - virtual pet
**Shishimanu is a Pygame-based virtual pet.**
It’s a lightweight, interactive package where you can run a pet on your desktop, experiment with animations, and extend it into your own projects.

## ✨ Features
- 🐾 Virtual Pet with idle, move, and interactive animations.
- ⚡ Cross-platform (Windows/Linux/macOS, with transparency on Windows).
- 📦 Packaged Assets for easy fonts, sprites, and backgrounds.

## 🚀 Installation & Running
```bash
pip install git+https://github.com/Tirth3/OTTO.git
shishimanu
```

## ⚙️ Command Line Options
| Flags | Description|
| --t   | Background mode (0 = auto, 1 = black, 2 = transparent [Windows only]). |
| --speed | Sets pet movement speed (default = 100). |
| --nofullscreen | Run in windowed mode (default = fullscreen). |
| --wsize | Window size in pixels (default 600). |
| --wpos X Y | Window position on screen (default = 100 100). |

## Roadmap
- Add pet stats (hunger, fun, sleep, health).
- Smarter roaming and AI-driven movement.
- Interaction mechanics (feeding, playing, etc).
- Save/load pet state.
- Resolution scaling improvements.

## 📦 Standalone Build
You can package it into a single executable using PyInstaller:
```bash
pyinstaller --onefile --noconsole -n shishimanu shishimanu/main.py
```

## ⚠️ Troubleshooting
* Transparent Background not working (Linux/macOS) :
  * Transparency (--t 2) only works on Windows via pywin32.
  * On other platforms, the window will fall back to black background.
* pip install fails with win32api not found :
    Install pywin32 separately (Windows only)
  ```bash
  pip install pywin32
  ```
* Warning about Scripts folder not in path :
  Follow the following guide.
