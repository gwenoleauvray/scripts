# mousePosition.py

Affiche en continu la position de la souris à l'écran, en pixels. Sert à trouver les coordonnées à donner à PyAutoGUI (par exemple l'endroit d'un bouton à cliquer).

## Prérequis

- PyAutoGUI installé avec [`installPyautogui`](installPyautogui.md).
- Une session graphique X11.

## Utilisation

```bash
~/.venvs/pyautogui/bin/python mousePosition.py
```

L'affichage se met à jour sur la même ligne :

```
Ctrl-C pour quitter.
X:  812  Y:  455
```

- `X` : distance depuis le bord gauche de l'écran.
- `Y` : distance depuis le haut de l'écran.
- `(0, 0)` est le coin en haut à gauche.

Appuyer sur **Ctrl-C** pour quitter.

## Ce que le script modifie

Rien : il ne fait que lire la position de la souris.
