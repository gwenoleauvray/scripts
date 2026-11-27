# Manuels des scripts

Un manuel par script : à quoi il sert, ce qu'il faut avant, comment le lancer, ce qu'il change sur la machine, et comment revenir en arrière.

**Règle d'or : relisez un script avant de le lancer**, surtout s'il utilise `sudo`. L'outil [`verify_script`](verify_script.md) peut vous aider.

## Scripts à jour

| Script | Rôle | Manuel |
|---|---|---|
| `checkJava4Shell` | Sécurité : cherche la faille Java4Shell sur toute la machine | [checkJava4Shell.md](checkJava4Shell.md) |
| `installPyautogui` | Installe PyAutoGUI (pilotage souris/clavier) | [installPyautogui.md](installPyautogui.md) |
| `updatePyautogui` | Met à jour PyAutoGUI | [updatePyautogui.md](updatePyautogui.md) |
| `configPyautogui.py` | Vérifie et règle PyAutoGUI, petits essais | [configPyautogui.md](configPyautogui.md) |
| `mousePosition.py` | Affiche la position de la souris | [mousePosition.md](mousePosition.md) |
| `installPyTesseract` | Installe la reconnaissance de texte Tesseract | [installPyTesseract.md](installPyTesseract.md) |
| `installPycharm` | Installe l'éditeur PyCharm (snap) | [installPycharm.md](installPycharm.md) |
| `installPycharmTarball` | Installe ou met à jour PyCharm sans snap | [installPycharmTarball.md](installPycharmTarball.md) |
| `installWaydroid` | Installe Android sous Linux | [installWaydroid.md](installWaydroid.md) |
| `installAndroidKVM` | Android dans une machine virtuelle KVM | [installAndroidKVM.md](installAndroidKVM.md) |
| `installVirtualbox` | Installe VirtualBox (dépôt Oracle) | [installVirtualbox.md](installVirtualbox.md) |
| `ai/verify_script.py` | IA : relit un script avant exécution | [verify_script.md](verify_script.md) |
| `ai/ocr_ai.py` | IA : lit le texte d'une image | [ocr_ai.md](ocr_ai.md) |
| `ai/claude_client.py` | Brique commune des outils IA | [claude_client.md](claude_client.md) |

## Anciens noms

| Ancien script | Devenu |
|---|---|
| `installPycharm1` | `installPycharmTarball` |
| `installPyautoguiOK` | `updatePyautogui` |
| `configPyautogui` | `configPyautogui.py` |
| `installAnboxPlayStore` | `installAndroidKVM` (et `installWaydroid`) |
| `installVirtualboxDebian9` | `installVirtualbox` |

## Lancer un script

```bash
git clone https://github.com/gwenoleauvray/scripts && cd scripts
chmod +x installPyautogui        # une seule fois, si le script n'est pas exécutable
./installPyautogui
```
