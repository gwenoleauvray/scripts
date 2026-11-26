# installWaydroid

Installe **Waydroid**, qui fait tourner Android et ses applications dans une fenêtre sous Linux. Remplace `installAnboxPlayStore` : Anbox est abandonné depuis 2023.

## Prérequis

- Debian 11 (bullseye), 12 (bookworm), 13 (trixie), 14 (forky) ou sid. Les autres distributions sont refusées.
- Une **session Wayland** et un noyau avec le module **binder**.
- Une machine physique de préférence. Waydroid fonctionne mal dans une machine virtuelle VirtualBox ; un hôte KVM avec accélération graphique convient mieux.

## Utilisation

| Commande | Effet |
|---|---|
| `./installWaydroid` | Installe seulement le paquet Waydroid. |
| `WAYDROID_INIT=1 ./installWaydroid` | Installe, puis télécharge Android sans les services Google. |
| `WAYDROID_INIT=1 WAYDROID_GAPPS=1 ./installWaydroid` | Pareil, avec les services Google (Play Store). |

## Ce que le script modifie

1. Lit la version de Debian dans `/etc/os-release`.
2. Installe `curl` et `ca-certificates`.
3. Installe Waydroid selon la version :
   - **Debian 13** : ajoute le dépôt `trixie-backports` dans `/etc/apt/sources.list.d/` et installe depuis celui-ci ;
   - **Debian 14 / sid** : installe directement ;
   - **Debian 11 / 12** : ajoute le dépôt officiel `repo.waydro.id`. ⚠ Cette étape télécharge un script et l'exécute en administrateur : relisez-le avant si vous le pouvez.
4. Avec `WAYDROID_INIT=1` : télécharge l'image Android, puis active le service `waydroid-container` au démarrage.

Le script s'arrête à la première erreur.

## Après l'installation

```bash
sudo waydroid init               # si pas fait par le script (ajouter -s GAPPS pour Google Play)
waydroid session start           # démarre Android
waydroid show-full-ui            # affiche l'écran Android
```

## Désinstaller

```bash
sudo systemctl disable --now waydroid-container
sudo apt remove waydroid
```

## Dépannage

- **« Distribution non gérée »** : votre système n'est pas dans la liste des prérequis. Voir https://docs.waydro.id.
- **Écran noir ou rien ne s'affiche** : vérifier qu'on est sous Wayland avec `echo $XDG_SESSION_TYPE`. La réponse doit être `wayland`.
