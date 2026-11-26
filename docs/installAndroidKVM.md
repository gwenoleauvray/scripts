# installAndroidKVM

Prépare la virtualisation **KVM** et crée une **machine virtuelle Android** à partir d'une image ISO.

*Remplace l'ancien brouillon `installAnboxPlayStore`.*

## Waydroid ou KVM ?

| | [`installWaydroid`](installWaydroid.md) | `installAndroidKVM` |
|---|---|---|
| Principe | Android partage le noyau Linux | Android dans une vraie machine virtuelle |
| Il faut | Session Wayland, noyau avec binder | Processeur avec virtualisation (VT-x / AMD-V) |
| Rapidité | Très rapide | Plus lourd (mémoire réservée) |
| Quand le choisir | En premier | Si Waydroid n'est pas possible (session X11…) |

## Prérequis

- Un PC **x86-64** avec la virtualisation activée dans le BIOS/UEFI (Intel VT-x ou AMD-V).
- Debian ou Ubuntu, avec les droits `sudo`.
- Pour la VM : une **image ISO Android x86-64**, à télécharger vous-même sur le site officiel du projet (par exemple Bliss OS ou Android-x86). Le script ne télécharge aucune image.

## Utilisation

| Commande | Effet |
|---|---|
| `./installAndroidKVM` | Installe KVM seulement. |
| `./installAndroidKVM ~/Téléchargements/android.iso` | Installe KVM et crée la VM. |

Réglages de la VM, à mettre devant la commande :

| Variable | Défaut | Rôle |
|---|---|---|
| `VM_NAME` | `android` | Nom de la VM |
| `VM_RAM` | `4096` | Mémoire, en Mo |
| `VM_CPUS` | `2` | Nombre de processeurs |
| `VM_DISK` | `16` | Disque, en Go |

```bash
VM_NAME=bliss VM_RAM=6144 ./installAndroidKVM ~/Téléchargements/Bliss.iso
```

## Ce que le script modifie

1. Vérifie le processeur et la présence de l'image.
2. Installe `qemu-system-x86`, `qemu-utils`, `libvirt-daemon-system`, `libvirt-clients`, `virtinst` et `virt-manager`.
3. Ajoute votre compte aux groupes `libvirt` et `kvm` : vous pourrez gérer les VM sans `sudo` **après vous être déconnecté puis reconnecté**.
4. Démarre le réseau virtuel `default` et le règle pour qu'il démarre tout seul.
5. Avec une image :
   - refuse d'écraser une VM du même nom ;
   - copie l'image dans `/var/lib/libvirt/images/` (le service des VM ne peut pas lire votre dossier personnel) ;
   - crée la VM avec un disque au format qcow2, et la démarre sur l'image.

## Après la création

```bash
virt-manager
```

Double-cliquer sur la VM, puis suivre l'installation d'Android dans sa fenêtre. Une fois Android installé, retirer l'image ISO dans les réglages de la VM (« CDROM ») pour démarrer sur le disque.

## Supprimer la VM

```bash
sudo virsh destroy android                          # l'arrête si elle tourne
sudo virsh undefine android --remove-all-storage    # la supprime avec son disque
```

## Dépannage

- **« La virtualisation matérielle est absente ou désactivée »** : l'activer dans le BIOS/UEFI (option « Intel Virtualization Technology », « SVM » ou « AMD-V »).
- **« Une VM nommée … existe déjà »** : choisir un autre nom avec `VM_NAME=`.
- **Écran noir au démarrage de la VM** : dans virt-manager, essayer une autre carte vidéo (« Video » → QXL ou VGA).
