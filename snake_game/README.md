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
Ce projet Snake a été mon tout premier exercice de programmation.

Au début, le jeu n’était qu’un simple serpent qui mangeait des pommes — rien de très élaboré. Mais je l’ai construit seule, en tâtonnant, en apprenant à chaque étape, en modifiant petit à petit chaque détail. C’est pour cela qu’il a une valeur très particulière pour moi.

Depuis des années, je n’ai cessé d’apprendre et d’approfondir mes connaissances en programmation.

Récemment, après avoir traversé une période de doute et de remise en question, j’ai ressenti le besoin de revenir à ce projet. Pas pour prouver quelque chose aux autres, mais pour me retrouver, revenir à l’essentiel, me recentrer.

J’ai repris le code, réorganisé la logique, ajouté des éléments visuels, des détails, des messages. Chaque ligne que je tapais me rappelait mes débuts : la joie quand le programme fonctionnait enfin, la frustration quand un bug restait introuvable.

Cette expérience a été faite de hauts et de bas, mais aussi de progression.

Ce projet n’est pas parfait. Mais il est sincère.  Il représente mes débuts, mes doutes, mes efforts.
  
Il est le signe que, même après avoir été un peu perdue, je peux continuer à avancer.  Et surtout, que je veux continuer à apprendre.

Heureusement, il existe la programmation.

Heureusement, je peux, avec quelques lettres, créer un monde à moi.
