# installVirtualboxDebian9 — ancienne version

> ⚠ **Obsolète, à ne pas lancer sur une Debian récente.** Voir le dépôt GitHub `installVirtualbox`.

Script d'installation de VirtualBox 6.0 pour Debian 9 « stretch », conservé pour mémoire.

## Ce qu'il fait

1. Met à jour **tous** les paquets du système (`apt-get upgrade`).
2. Ajoute le dépôt VirtualBox d'Oracle pour Debian 9 dans `/etc/apt/sources.list.d/virtualbox.list`.
3. Ajoute les clés de signature d'Oracle avec `apt-key`.
4. Installe `virtualbox-6.0`.

## Pourquoi ne plus l'utiliser

- Debian 9 est en fin de vie, et VirtualBox 6.0 n'est plus maintenu.
- `apt-key` est supprimé des Debian récentes : l'étape 3 échoue.
- Le dépôt est déclaré en `http://`, non chiffré.

## Si vous l'avez lancé par erreur

```bash
sudo rm /etc/apt/sources.list.d/virtualbox.list
sudo apt update
```
