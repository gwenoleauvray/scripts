#!/usr/bin/env python3
"""Affiche en continu la position de la souris (utile pour calibrer PyAutoGUI). Ctrl-C pour quitter.

Usage  : ~/.venvs/pyautogui/bin/python mousePosition.py
Prérequis : PyAutoGUI installé (./installPyautogui), session graphique X11.
Manuel : docs/mousePosition.md
"""
import sys
import time

import pyautogui

print("Ctrl-C pour quitter.")
try:
    # Boucle sans fin : lit la position et la réécrit sur la même ligne.
    while True:
        x, y = pyautogui.position()  # coordonnées en pixels, (0, 0) = coin haut gauche
        # « \r » ramène le curseur en début de ligne : l'affichage se met à jour sur place.
        print(f"\rX: {x:4d}  Y: {y:4d}", end="", flush=True)
        time.sleep(0.05)  # évite de saturer le CPU
except KeyboardInterrupt:
    # Ctrl-C : on passe à la ligne et on quitte proprement.
    print()
    sys.exit(0)
