# scripts

Scripts d'installation pour une VM de travail **PyAutoGUI / OCR / Android** sous Debian, plus des outils avec **IA (Claude)**.
Install scripts for a PyAutoGUI / OCR / Android Debian VM, plus Claude-powered helpers.

**Relisez les scripts avant de les lancer — aucune garantie.** / Please review scripts before use. No warranty.

📖 **Manuels en français pour chaque script : [docs/](docs/README.md)**

| Script | Rôle |
|---|---|
| `installPyautogui` | PyAutoGUI dans un venv (`~/.venvs/pyautogui`) — X11 uniquement |
| `installPyTesseract` | Tesseract OCR (fra+eng) + pytesseract dans un venv (`~/.venvs/ocr`) |
| `updatePyautogui` | Met à jour PyAutoGUI et ses dépendances dans son venv (sans sudo) |
| `configPyautogui.py` | Vérifie PyAutoGUI (écran, souris, FAILSAFE) ; essais `--test` et `--ecrire` |
| `installPycharm` | PyCharm via snap (le snap `pycharm-community` installe désormais le PyCharm unifié) |
| `installPycharmTarball` | PyCharm sans snap, archive officielle JetBrains vérifiée (SHA-256) ; relancer = mettre à jour |
| `installWaydroid` | Android sous Linux (remplace Anbox, abandonné en 2023) |
| `installAndroidKVM` | KVM + machine virtuelle Android à partir d'une image ISO x86-64 |
| `installVirtualbox` | VirtualBox 7.2 depuis le dépôt Oracle (clé vérifiée, `signed-by`) — Debian 11–13, Ubuntu 22.04–25.10 |
| `checkJava4Shell` | Sécurité : cherche Java4Shell (CVE-2026-114938) sur toute la machine — versions de Java, processeur, plantages, traces d'attaque. Lecture seule, `sudo bash checkJava4Shell` |
| `mousePosition.py` | Affiche la position de la souris pour calibrer PyAutoGUI |
| `ai/verify_script.py` | **IA** : relit un script shell (analyse locale + revue Claude) avant exécution |
| `ai/ocr_ai.py` | **IA** : OCR Tesseract, correction par Claude (`--clean`) ou lecture directe de l'image (`--vision`) |

## Outils IA
```bash
python3 -m venv ~/.venvs/ai && ~/.venvs/ai/bin/pip install -r ai/requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."        # clé API Anthropic
# export ANTHROPIC_MODEL=claude-sonnet-5-5   # modèle (défaut), modifiable

~/.venvs/ai/bin/python ai/verify_script.py --offline installPycharm   # analyse locale, rien n'est envoyé
~/.venvs/ai/bin/python ai/verify_script.py installPycharm             # + revue par Claude
~/.venvs/ai/bin/python ai/ocr_ai.py capture.png --clean
```
⚠ Les fonctions IA envoient le contenu du script / du texte / de l'image à l'API Anthropic. `verify_script.py` refuse d'envoyer un fichier qui semble contenir un secret.

## Ce qui a changé par rapport à la v1
- `pip3 install python3-xlib` (paquet inexistant sous pip) → `python-xlib`, et installation en venv (Debian 12+ bloque pip en global, PEP 668)
- `installPyTesseract` : mélangeait bash et Python, et n'installait pas le binaire `tesseract` → corrigé
- `installAnboxPlayStore` (inachevé, Anbox abandonné) → `installWaydroid`, et `installAndroidKVM` pour Android en machine virtuelle
- Les 5 anciens scripts ont été réécrits avec un nouveau rôle chacun :
  `installPycharm1` → `installPycharmTarball`, `installPyautoguiOK` → `updatePyautogui`,
  `configPyautogui` (bash/Python mélangés) → `configPyautogui.py`,
  `installAnboxPlayStore` → `installAndroidKVM`, `installVirtualboxDebian9` (Debian 9, `apt-key`) → `installVirtualbox`
