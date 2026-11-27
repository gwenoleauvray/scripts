# installVirtualbox

Installe **VirtualBox** depuis le dépôt officiel d'Oracle, sur une Debian ou une Ubuntu récente.

*Remplace l'ancien `installVirtualboxDebian9` (Debian 9, VirtualBox 6.0, `apt-key`).*

## Prérequis

- Un PC **x86-64** : Oracle ne publie pas VirtualBox pour ARM (donc pas pour Raspberry Pi).
- Un de ces systèmes : Debian 11 (bullseye), 12 (bookworm), 13 (trixie) ; Ubuntu 22.04 (jammy), 24.04 (noble), 25.04 (plucky), 25.10 (questing).
- Les droits `sudo`.

## Utilisation

```bash
./installVirtualbox
```

Pour une autre branche que la 7.2 :

```bash
VBOX_VERSION=7.1 ./installVirtualbox
```

## Ce que le script modifie

1. Vérifie le processeur et la version du système.
2. S'arrête si le paquet `virtualbox` de la distribution est déjà installé (les deux entrent en conflit).
3. Installe `curl`, `gpg` et de quoi compiler le module noyau de VirtualBox (`gcc`, `make`, `perl`, en-têtes du noyau).
4. Télécharge la clé de signature d'Oracle et **vérifie son empreinte** (`B9F8 D658 297A F3EF C18D 5CDF A2F6 83C5 2980 AECF`). Si elle ne correspond pas, il arrête tout.
5. Range la clé dans `/usr/share/keyrings/oracle-virtualbox-2016.gpg`, utilisée **seulement** pour ce dépôt (`signed-by`).
6. Déclare le dépôt dans `/etc/apt/sources.list.d/virtualbox.list`, en HTTPS. Ce fichier remplace celui laissé par l'ancien script.
7. Installe `virtualbox-7.2`.
8. Ajoute votre compte au groupe `vboxusers`, pour l'USB dans les VM, **après vous être déconnecté puis reconnecté**.
9. Prévient si Secure Boot est actif.

## Après l'installation

```bash
virtualbox
```

Ou depuis le menu des applications.

## Secure Boot

Avec Secure Boot actif, le noyau refuse les modules non signés et les VM ne démarrent pas (erreur « vboxdrv »). Deux solutions :

- désactiver Secure Boot dans le BIOS/UEFI ;
- ou signer le module avec votre propre clé MOK, enregistrée au redémarrage suivant (voir la page « SecureBoot » du wiki Debian).

## Si l'ancien script avait été lancé

L'ancien `installVirtualboxDebian9` avait ajouté des clés Oracle avec `apt-key`. Elles ne servent plus. Pour voir s'il en reste :

```bash
ls /etc/apt/trusted.gpg /etc/apt/trusted.gpg.d/ 2>/dev/null
```

## Désinstaller

```bash
sudo apt remove virtualbox-7.2
sudo rm /etc/apt/sources.list.d/virtualbox.list /usr/share/keyrings/oracle-virtualbox-2016.gpg
sudo apt update
```

Vos machines virtuelles restent dans `~/VirtualBox VMs/`.

## Dépannage

- **« En-têtes du noyau introuvables »** : installer les en-têtes de votre noyau, puis lancer `sudo /sbin/vboxconfig`.
- **« Système non publié par Oracle »** : votre version n'est pas dans la liste des prérequis. Voir https://www.virtualbox.org/wiki/Linux_Downloads.
