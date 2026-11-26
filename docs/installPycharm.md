# installPycharm

Installe **PyCharm**, l'éditeur de code Python de JetBrains, par le système de paquets **snap**.

Depuis la version 2025.3, le snap `pycharm-community` installe le PyCharm unifié (gratuit, Jupyter inclus) : l'édition Community séparée n'existe plus.

## Prérequis

- Debian ou Ubuntu, avec les droits `sudo`.

## Utilisation

```bash
./installPycharm
```

## Ce que le script modifie

1. Installe `snapd`, le gestionnaire de snaps.
2. Sous Debian, crée le lien `/snap` vers `/var/lib/snapd/snap`, s'il n'existe pas. Les snaps « classic » en ont besoin.
3. Installe PyCharm en mode `--classic` : il a accès à tout le système de fichiers, ce qui est nécessaire pour un éditeur de code.

Le script s'arrête à la première erreur.

## Après l'installation

Lancer PyCharm depuis le menu des applications, ou :

```bash
/snap/bin/pycharm-community
```

Les snaps se mettent à jour tout seuls.

## Désinstaller

```bash
sudo snap remove pycharm-community
```

## Dépannage

- **PyCharm n'apparaît pas dans le menu** : se déconnecter puis se reconnecter à la session.
