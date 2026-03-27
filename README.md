# Projet d'analyse OSINT et extraction de données Android

## Présentation du projet

Ce projet a pour objectif de présenter les différentes méthodes permettant :

1. **d'extraire des données depuis un téléphone Android**
2. **d'utiliser ces informations pour effectuer des recherches dans des bases de données publiques et des sources ouvertes**


Le projet est donc divisé en deux parties principales :

- **Partie 1 : Recherche OSINT à partir des informations collectées**
- **Partie 2 : Extraction et analyse des données d’un téléphone Android**
- **Partie 3 : Minilab OSINT pour faire des recherches**

⚠️ Les méthodes présentées dans ce projet doivent être utilisées **dans un cadre légal et éthique**, notamment dans les domaines :

- cybersécurité
- investigation numérique
- analyse forensic
- formation et recherche

---


# Partie 1 - Recherche OSINT à partir d'informations trouvées sur un téléphone

Lorsqu'un téléphone est analysé, plusieurs types d'informations peuvent être retrouvées :

- numéro de téléphone
- adresse email
- pseudo / nom d'utilisateur
- photos
- nom réel
- entreprise
- comptes réseaux sociaux

Ces informations peuvent ensuite être utilisées pour effectuer des recherches dans des **bases de données publiques et des services OSINT**.

---

# 1. Recherche à partir d’un numéro de téléphone

Les annuaires publics permettent parfois d’identifier le propriétaire d’un numéro de téléphone ou une entreprise associée.

### Annuaires inversés

- https://www.118712.fr/
- https://www.pagesjaunes.fr/

Ces services permettent de retrouver :

- un nom associé à un numéro
- une adresse
- une activité professionnelle

### Informations et signalements sur un numéro

- https://www.tellows.fr/

Ce site permet de consulter :

- les signalements d’utilisateurs
- la réputation d’un numéro
- le type d’appel (spam, démarchage, etc.)

---

# 2. Recherche à partir d’une adresse email

Une adresse email peut être utilisée pour identifier des comptes ou vérifier si elle apparaît dans des bases de données publiques.

### Outils

- https://epieos.com/
- https://hunter.io/
- https://haveibeenpwned.com/

Ces services permettent de :

- vérifier si l'email apparaît dans une fuite de données
- retrouver des comptes associés
- identifier un domaine professionnel

---

# 3. Recherche à partir d’un pseudo / nom d’utilisateur

Les utilisateurs réutilisent souvent le même pseudonyme sur plusieurs sites internet.

### Outils utiles

- https://namechk.com
- https://whatsmyname.app
- https://usersearch.org

Ces outils permettent de vérifier la présence d’un pseudo sur :

- réseaux sociaux
- forums
- plateformes web
- services en ligne

---

# 4. Recherche sur les réseaux sociaux

Les informations extraites d’un téléphone peuvent être recherchées directement sur les réseaux sociaux.

Plateformes principales :

- https://facebook.com
- https://instagram.com
- https://linkedin.com
- https://twitter.com

Ces plateformes peuvent fournir :

- identité
- relations
- localisation
- activité professionnelle
- photos

---

# 5. Recherche à partir d’une image

Une photo trouvée sur un téléphone peut contenir :

- des métadonnées
- une localisation
- un visage
- un lieu identifiable

La recherche inversée d’image permet de retrouver l'origine d'une photo.

### Outils

- https://images.google.com
- https://tineye.com
- https://yandex.com/images

Ces outils permettent de retrouver :

- les sites où l'image apparaît
- les profils utilisant la même photo
- l'origine possible de l'image

---

# 6. Recherche d’identité ou d’entreprise en France

Si un nom ou une entreprise est trouvé dans un téléphone, il peut être vérifié dans les bases publiques françaises.

### Registres officiels

- https://www.infogreffe.fr
- https://www.societe.com
- https://annuaire-entreprises.data.gouv.fr
- https://www.pappers.fr/

Ces bases permettent de retrouver :

- dirigeants d’entreprise
- adresse d’une société
- statut juridique
- informations financières

---

# 7. Données publiques françaises (Open Data)

Le portail officiel de données ouvertes du gouvernement français.

https://www.data.gouv.fr

Il contient des milliers de bases de données publiques sur :

- entreprises
- associations
- administrations
- statistiques publiques

---

# 8. OSINT Framework

https://osintframework.com/

L'OSINT Framework est un répertoire regroupant **des centaines d’outils OSINT** classés par catégorie :

- recherche de personnes
- réseaux sociaux
- emails
- domaines
- documents
- images
- géolocalisation

---

# Partie 2 - Extraction de données à partir d’un téléphone Android

L'analyse d'un téléphone Android permet d'extraire de nombreuses informations qui peuvent ensuite être analysées dans le cadre d'une investigation numérique.

Cette discipline est appelée **Mobile Forensics**.

Les données récupérées peuvent inclure :

- contacts
- messages SMS
- historique d'appels
- fichiers
- photos
- comptes utilisateurs
- applications installées
- données système

---

# 1. Android Debug Bridge (ADB)

ADB est un outil officiel permettant de communiquer avec un appareil Android via USB ou réseau.

Fonctions principales :

- accéder au système de fichiers
- installer ou désinstaller des applications
- récupérer certains fichiers
- exécuter des commandes sur l'appareil

# 1.1 Guide d'installation

# 1.1.1 Windows

1. Télécharger les SDK Platform-Tools pour [Windows](https://developer.android.com/tools/releases/platform-tools?hl=fr)

2. Extraire le fichier zip SDK

3. Ajouter au PATH :

    - Chercher "Modifier les variables d'environnement système" dans Windows.

    - Aller dans Variables d'environnement.

    - Dans "Variables système", ajouter le chemin de votre dossier (ex: C:\adb). 

4. Pour vérifier, ouvrir un terminal (PowerShell ou CMD) et taper : ```adb --version```.

# 1.1.2 MacOS

**Via Homebrew :**
Dans Terminal :

```brew install --cask android-platform-tools```

**Manuellement :**
1. Télécharger les SDK Platform-Tools pour [Mac](https://developer.android.com/tools/releases/platform-tools?hl=fr)

2. Extraire le dossier.

3. Ajouter le chemin au profil Zsh :

```echo 'export PATH=$PATH:/chemin/vers/votre/dossier/platform-tools' >> ~/.zshrc```

```source ~/.zshrc```

# 1.1.3 Linux

```sudo apt update```

```sudo apt install android-tools-adb android-tools-fastboot```

# 1.2 Guide d'utilisation 

# 1.2.1 Activer mod debug sur android

- Aller dans Paramètres > À propos et taper 7 fois sur "Numéro de build".

- Aller dans Paramètres > Système > Options pour les développeurs et cocher "Débogage USB".

- Brancher le téléphone au PC. Une fenêtre s'ouvrira sur le téléphone demandant d'autoriser l'ordinateur. Cocher "Toujours" puis valider.

# 1.2.2 

- Activer mod debug sur le smatphone android

- Vérifier la connexion avec : ```adb devices```

- Passer en mode root : ```adb root```

- Utiliser shell du système du smartphone : ```adb shell```

- Utiliser commande abd + shell :
```adb shell``` + votre commande shell

---

# Partie 3 - Minilab OSINT

Ce mini-lab OSINT est un environnement Python léger pour effectuer des recherches publiques sur des utilisateurs, adresses e-mail ou numéros de téléphone.
Il inclut des outils gratuits et simples à utiliser, ainsi que des bibliothèques Python pour analyser et visualiser les données collectées.



---

### Installation

1. **Exécuter le script d'installation**

```bash
bash lab.sh
```

2. **Activer l'environnement**

```bash
source ~/MINI_LAB_OSINT/venv/bin/activate
```

---

### Outils inclus et documentation

| Outil | Description | Documentation |
|---|---|---|
| **Maigret** | Recherche un pseudonyme sur +500 sites | [GitHub](https://github.com/soxoj/maigret) |
| **Sherlock** | Recherche de comptes sur les réseaux sociaux | [GitHub](https://github.com/sherlock-project/sherlock) |
| **Holehe** | Vérifie si une adresse e-mail existe sur des services en ligne | [GitHub](https://github.com/megadose/holehe) |
| **PhoneInfoga** | Recherche OSINT sur un numéro de téléphone | [GitHub](https://github.com/sundowndev/phoneinfoga) |
| **googlesearch-python** | Automatisation des recherches Google | [PyPI](https://pypi.org/project/googlesearch-python/) |
| **Requests** | Faire des requêtes HTTP simples | [Docs Requests](https://requests.readthedocs.io/) |
| **BeautifulSoup4** | Extraire et parser du contenu HTML | [Docs BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) |
| **Pandas** | Manipuler et analyser CSV/JSON | [Pandas](https://pandas.pydata.org/docs/) |
| **Folium** | Créer des cartes interactives | [Folium](https://python-visualization.github.io/folium/) |
| **NetworkX** | Créer et visualiser des graphes simples | [NetworkX](https://networkx.org/documentation/stable/) |
| **python-whois** | Récupérer info domaine/IP | [PyPI](https://pypi.org/project/python-whois/) |


