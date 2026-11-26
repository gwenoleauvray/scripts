# installPyautoguiOK — ancienne version

> ⚠ **Obsolète.** Utiliser [`installPyautogui`](installPyautogui.md).

Première version du script d'installation de PyAutoGUI, conservée pour mémoire.

## Ce qu'il fait

1. Met à jour **tous** les paquets du système (`apt-get upgrade`).
2. Installe `python3-pip`, `scrot`, `python3-tk` et `python3-dev`.
3. Installe `python3-xlib` et `pyautogui` avec `pip3`, pour tout le système.

## Pourquoi ne plus l'utiliser

- Debian 12 et plus récents **refusent** `pip3 install` pour tout le système. La nouvelle version installe dans un environnement virtuel.
- Le paquet pip `python3-xlib` n'existe pas ; le bon nom est `python-xlib`.
- Il continue même si une étape échoue.
