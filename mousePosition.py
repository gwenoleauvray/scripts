#!/usr/bin/env python3
"""Affiche en continu la position de la souris (utile pour calibrer PyAutoGUI). Ctrl-C pour quitter."""
import sys
import time

import pyautogui

print("Ctrl-C pour quitter.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"\rX: {x:4d}  Y: {y:4d}", end="", flush=True)
        time.sleep(0.05)  # évite de saturer le CPU
except KeyboardInterrupt:
    print()
    sys.exit(0)
