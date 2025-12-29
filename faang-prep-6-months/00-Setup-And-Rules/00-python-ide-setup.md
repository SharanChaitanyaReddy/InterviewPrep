# Python & IDE Setup

Install VS-code as IDE

Python 3.12 Installation (Week-1 Minimal Setup)
STEP 1: Download Python (Official Source Only)

👉 Open browser
👉 Go to: python.org
👉 Click Downloads

You will see:

Python 3.12.x (recommended)

Download the installer for your OS.
 Windows Installation
 (Windows): Install Python (Very Important Options)

Open the downloaded .exe

CHECK THIS BOX FIRST ✅
👉 “Add Python 3.12 to PATH”

Click Install Now

Finish installation


🖥️ A) macOS Installation
STEP 2 (macOS): Install Python

Open the downloaded .pkg file

Click Continue → Continue → Agree

Install with default settings

Finish installation

⚠️ macOS already has Python 2.x / old Python — ignore it, we’ll use Python 3.12.

STEP 3 (macOS): Verify Installation

Open Terminal and run:

python3 --version

Expected output:

Python 3.12.x

Also check pip:

pip3 --version

If both work → ✅ good.


STEP 4: Verify Python Inside VS Code

Open VS Code

Create a new file:

test.py


Add this code:

print("Python setup successful 🚀")


Open VS Code terminal
(View → Terminal)

Run:

python test.py


or on mac:

python3 test.py


Expected output:

Python setup successful 🚀


✅ This confirms:

Python installed

VS Code can run Python

Terminal PATH is correct

STEP 5: Select Python Interpreter in VS Code (One-Time)

In VS Code:

Press Cmd + Shift + P (Mac)
or Ctrl + Shift + P (Windows)

Search: Python: Select Interpreter

Choose Python 3.12.x

This avoids confusion later.


Small Motivation (Not Cheesy)

“Strong systems are built by setting foundations once — correctly.”