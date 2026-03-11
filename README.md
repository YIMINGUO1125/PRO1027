# PRO1027 – Travail Pratique #1  
## Système de neutralisation de nœuds de corruption

> Projet réalisé dans le cadre du cours **PRO1027 – Programmation scientifique en C**  
> Session : **Hiver 2026**

---

## Table des matières
- [Description](#description)
- [Objectifs](#objectifs)
- [Informations importantes](#informations-importantes)
- [Contraintes techniques](#contraintes-techniques)
- [Structure du projet](#structure-du-projet)
- [Répartition des tâches](#répartition-des-tâches)
- [Fonctionnalités à implémenter](#fonctionnalités-à-implémenter)
- [Installation et exécution](#installation-et-exécution)
- [Tests à réaliser](#tests-à-réaliser)
- [Rapport à remettre](#rapport-à-remettre)
- [Critères d’évaluation](#critères-dévaluation)
- [Avancement](#avancement)
- [Membres de l’équipe](#membres-de-léquipe)

---

## Description
Ce projet consiste à développer une application console en **Python 3 avec NumPy**.  
Le programme génère une grille binaire secrète, calcule les indices des lignes et des colonnes, puis permet de résoudre le puzzle selon deux modes :

- **Mode manuel**
- **Mode algorithmique (IA)**

Le thème retenu est un style **cybersécurité / système corrompu**, avec une interface console utilisant des symboles et des couleurs ANSI.

---

## Objectifs
Ce travail pratique vise à mettre en application :

- la manipulation de matrices avec **NumPy**
- les structures de données multidimensionnelles
- la résolution de systèmes linéaires sous la forme **AX = B**
- la conception d’une petite application modulaire en Python
- l’organisation d’un projet en équipe

---

## Informations importantes
- **Cours** : PRO1027 – Programmation scientifique en C
- **Travail** : TP #1
- **Remise** : **11 mars 2026 à 23h55**
- **Pondération** : **15 %**
- **Équipe** : **3 à 5 étudiants**
- **Fichier à remettre** : **un seul fichier `.zip`**
- **Contenu du `.zip`** :
  - tous les fichiers `.py`
  - le rapport final

---

## Contraintes techniques
- Langage autorisé : **Python 3**
- Bibliothèque autorisée : **NumPy**
- Aucun autre langage n’est permis
- Aucune autre bibliothèque tierce ne doit être nécessaire pour exécuter le projet

---

## Structure du projet
```text
PRO1027/
│── main.py
│── play.py
│── ui.py
│── solver.py
│── README.md
│── rapport.pdf
```

### Description des fichiers

#### `main.py`
Point d’entrée du projet.

#### `play.py`
Contient la logique principale du jeu :
- menu de difficulté
- choix du mode
- boucle principale
- interaction avec le joueur

#### `ui.py`
Contient l’interface console :
- affichage de la grille
- affichage des indices
- animation finale en cas d’échec

#### `solver.py`
Contient le solveur matriciel :
- construction de la matrice `A`
- construction du vecteur `B`
- résolution avec `np.linalg.lstsq()`

---

## Répartition des tâches
Comme nous sommes quatre, la répartition proposée est la suivante :

| Partie | Responsabilités | Responsable |
|--------|------------------|-------------|
| UI | `print_ui()` + `show_final_corruption()` | |
| Play | `play()` + `get_difficulty()` + logique du jeu ||
| Solver | `solve_with_numpy_step_by_step()` + résolution avec NumPy | |
| Main | intégration finale + tests + rapport | |

---

## Fonctionnalités à implémenter

### 1. Menu interactif
- affichage des niveaux de difficulté
- choix du mode :
  - manuel
  - IA

### 2. Génération du puzzle
- création d’une grille secrète binaire
- calcul des sommes cibles :
  - des lignes
  - des colonnes

### 3. Affichage console
- affichage de la zone sélectionnée
- affichage du temps restant
- affichage des indices de colonnes
- affichage des indices de lignes
- affichage des cellules avec des symboles comme :
  - `■` pour 1
  - `·` pour 0

### 4. Solveur NumPy
- transformer le puzzle en système `AX = B`
- créer la matrice de contraintes `A`
- créer le vecteur `B`
- résoudre avec `np.linalg.lstsq()`
- afficher les étapes du solveur dans la console

### 5. Gestion de l’échec
- déclencher une animation de type corruption / crash
- afficher un message final de perte de contrôle du système

---

## Installation et exécution

### 1. Installer NumPy
```bash
pip install numpy
```

### 2. Lancer le programme
```bash
python main.py
```

---

## Tests à réaliser

### Test 1 — Menu principal
- vérifier que le menu s’affiche correctement

### Test 2 — Cinq niveaux de difficulté
Pour chacun des **5 niveaux** :
- afficher la grille
- afficher les indices
- exécuter le mode IA
- montrer les étapes du bot dans la console

### Test 3 — Réussite en mode manuel
Au niveau le plus bas :
- trouver au moins **5 cases**
- faire au moins **1 erreur**
- reselectionner une case déjà choisie pour la désactiver
- montrer le temps restant et les informations affichées

### Test 4 — Échec en mode manuel
Au niveau le plus bas :
- effectuer au moins **2 actions**
- laisser le temps tomber à **0**
- afficher le résultat final et l’animation d’échec

### Test 5 — Mauvaise entrée
- saisir un input invalide
- vérifier la réaction du programme

---

## Rapport à remettre
Le rapport final doit contenir au minimum :

1. **Une page de présentation**
2. **Une page décrivant le rôle de chaque membre**
3. **Une section sur les problèmes et difficultés rencontrés**
4. **Une section guide utilisateur + preuves de tests**

Pour chaque test, il faut indiquer :
- le test effectué
- les étapes suivies
- les entrées utilisées
- le résultat attendu
- les hypothèses et tentatives en cas de problème

---

## Critères d’évaluation

| Élément | Points |
|--------|--------|
| Rapport complet / guide utilisateur / preuves de tests | 3 |
| `play()` | 2 |
| `get_difficulty()` | 2 |
| `show_final_corruption()` | 2 |
| `print_ui()` | 3 |
| `solve_with_numpy_step_by_step()` | 3 |

**Total : 15 points**

---

## Avancement
- [ ] Choix du thème visuel
- [ ] Menu interactif
- [ ] Génération de la solution secrète
- [ ] Calcul des indices
- [ ] Affichage console
- [ ] Gestion du mode manuel
- [ ] Gestion du mode IA
- [ ] Animation d’échec
- [ ] Tests complets
- [ ] Rapport final
- [ ] Compression `.zip` pour la remise

---

## Membres de l’équipe

| Nom | Code permanent | Rôle |
|-----|----------------|------|
|  | | UI |
|  | | Play |
|  | | Solver |
|  |  | Main / Tests / Rapport |

---

## Remarques
- Le code doit être commenté de manière pertinente
- Le projet doit être testé avant la remise
- L’intégration finale doit être vérifiée avant la création du `.zip`
- Tous les membres doivent connaître la structure du projet
