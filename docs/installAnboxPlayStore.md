# installAnboxPlayStore — brouillon inachevé

> ⚠ **Obsolète.** Utiliser [`installWaydroid`](installWaydroid.md) pour Android sous Linux.

Début de script pour installer Anbox (Android sous Linux) avec le Play Store, conservé pour mémoire. **Il s'arrête avant d'installer Anbox** : il ne pose que des outils.

## Ce qu'il fait

1. Met à jour **tous** les paquets du système (`apt-get upgrade`).
2. Installe `wget`, `lzip`, `unzip` et `squashfs-tools`, qui auraient servi à télécharger et décompresser l'image Android.
3. Installe `snapd`.

## Pourquoi ne plus l'utiliser

Anbox est abandonné depuis 2023. Waydroid l'a remplacé.
