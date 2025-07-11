# README# 🐍 Jeu du Serpent

## 📌 Présentation du projet

Ce projet est un mini-jeu du serpent développé en Python à l’aide de la bibliothèque graphique `pygame`.  
Les éléments visuels sont enrichis par des emojis, ce qui rend le jeu à la fois amusant et visuellement attrayant.  
Ce projet est idéal pour les débutants souhaitant pratiquer la conception d’interfaces graphiques, la logique orientée objet et la gestion des événements.

## 🎮 Règles du jeu

- Contrôle du serpent avec les touches fléchées (↑ ↓ ← →)  
- Le serpent se déplace case par case sur une grille  
- Apparition aléatoire de fruits : 🍓, 🥭, 🍐, 🥑  
- À chaque fruit mangé, un message “I like + fruit” s’affiche  
- Le serpent grandit, le score augmente  
- Collision avec le mur ou soi-même = fin du jeu

## 💻 Technologies utilisées

- Python : langage principal  
- pygame : interface graphique, boucle de jeu  
- pygame_emojis : pour charger les emojis comme images  
- Programmation orientée objet : classe `Snake`  
- Structures de données : listes, dictionnaires  
- Aléatoire : direction initiale, type de fruit

## 📂 Structure du projet

```

snake_game/
├── Snake/
│   └── Snake.py          # 🎮 Script principal du jeu 
├── assets/
│   └── snake_demo.mp4    # 🎥 Vidéo de démonstration du jeu
├── README.md             # 📄 Documentation du projet en chinois
├── README_fr.md          # 📄 Documentation du projet en français
├── requirements.txt      # 📦 Liste des dépendances Python 
└── .gitignore            # 🚫 Fichiers/dossiers à exclure du versionnage Git
```

## 🚀 Comment exécuter

1. Installer les dépendances :

```bash
pip install -r requirements.txt
```

2. Lancer le jeu :

```bash
python Snake/Snake.py
```

## 🔧 Améliorations prévues

- ✅ Remplacer les emojis par des images PNG  
- ✅ Ajouter une musique de fond et des sons  
- ✅ Créer un menu d’accueil et des niveaux  
- ✅ Sauvegarder les scores dans un classement

## 👩‍💻 À propos de l’autrice

Je suis une étudiante chinoise en France. J’aime la programmation et j’ai appris à coder en grande partie par moi-même.

## 🪄 Origine du projet

Ce projet est le tout premier que j’ai réalisé depuis que j’ai commencé à apprendre la programmation.

C’est un jeu de serpent que j’ai codé à mes débuts, lorsque je venais tout juste de découvrir Python.

Même s’il n’est pas très complexe, je l’ai construit petit à petit, en apprenant par moi-même, et en l’améliorant ligne par ligne.

Ces dernières années, j’ai toujours continué à apprendre davantage sur la programmation.

Récemment, j’ai traversé une période un peu difficile.
Après avoir pris le temps de me poser, j’ai décidé de rouvrir ce projet.
J’ai revu toute sa logique, ajouté des images, des détails, des messages, et corrigé ce qui ne fonctionnait pas.

À chaque ligne de code que je tapais, je repensais à mes débuts :
la joie quand le programme fonctionne enfin, et le découragement quand je ne trouve pas un bug.

Cette expérience a été faite de moments durs, mais aussi de moments heureux.

Heureusement, la programmation existe.

Heureusement, je peux construire un monde à moi avec quelques lettres.