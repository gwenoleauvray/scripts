# installPycharmTarball

Installe **PyCharm sans snap**, depuis l'archive officielle de JetBrains. Pour ceux qui préfèrent éviter snap ; sinon, [`installPycharm`](installPycharm.md) fait la même chose en une ligne.

*Remplace l'ancien `installPycharm1`.*

## Prérequis

- Debian ou Ubuntu, avec les droits `sudo`.
- Un PC x86-64 ou ARM64.
- Une connexion internet (l'archive pèse plusieurs centaines de Mo).

## Utilisation

```bash
./installPycharmTarball
```

À lancer en utilisateur normal, pas avec `sudo` devant : le script demande le mot de passe seulement quand il en a besoin.

Pour installer ailleurs que dans `/opt` :

```bash
INSTALL_DIR=~/logiciels ./installPycharmTarball
```

**Mettre à jour** : relancer simplement le script. Il ne fait rien si la dernière version est déjà installée.

## Ce que le script modifie

1. Installe `curl`, `python3`, `tar` et les bibliothèques graphiques demandées par JetBrains (`libxi6`, `libxrender1`, `libxtst6`, `mesa-utils`, `libfontconfig1`, `libgtk-3-bin`, `dbus-user-session`).
2. Demande à JetBrains le numéro de la dernière version publiée.
3. Télécharge l'archive et **vérifie son empreinte SHA-256**. Si elle ne correspond pas, il arrête tout.
4. Décompresse dans `/opt/pycharm-<version>`.
5. Crée la commande `pycharm` (lien `/usr/local/bin/pycharm`).
6. Ajoute PyCharm au menu des applications (`~/.local/share/applications/jetbrains-pycharm.desktop`).
7. Signale les anciennes versions restées dans `/opt`, sans les supprimer.

## Après l'installation

```bash
pycharm
```

Ou depuis le menu des applications. Au premier lancement, PyCharm propose 30 jours d'essai Pro, puis reste gratuit pour les fonctions de base.

## Désinstaller

```bash
sudo rm -rf /opt/pycharm-*
sudo rm /usr/local/bin/pycharm
rm ~/.local/share/applications/jetbrains-pycharm.desktop
```

Vos réglages restent dans `~/.config/JetBrains/` ; les supprimer aussi pour tout effacer.

## Dépannage

- **« Réponse inattendue de JetBrains »** : JetBrains a changé son service. Télécharger à la main sur https://www.jetbrains.com/pycharm/download/.
- **« L'empreinte SHA-256 ne correspond pas »** : téléchargement abîmé. Relancer le script.
