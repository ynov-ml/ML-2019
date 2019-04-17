# Git repos for ML at Ynov, Spring 2019.

Ajouter le liens à votre repo git avec texte qui vous identifie.
Tenir en ordre lexicographique par nom.

Vous voulez tous cloner ?  Rien n'est plus simple.  Dans un nouveau
répertoire non-contrôlé par git, tapez le suivant :

```
grep https /path/to/GIT.md | \
    tr -d '[]()'           | \
	sed -e 's/\(^.*https\)\(.*$\)/https\2::\L\1/;  s/https$//; s/ /-/g; s/::/  /; s/^/git clone /;'
```

## Les répertoires à créer (projets)

### Contrôles Continus

*Répertoire : ContrôleContinu*

Pour les contrôles continus qui sont en code.  Créez des fichiers avec
noms clairs pour chaque contrôle (ou créez un sous-répertoire, au choix).


### MNIST

*Répertoire : TP1_MNIST*

Utiliser une régression logistique (disponible dans scikit-learn) pour
construire un classifieur, et OvO et OvA, sur le jeu de données MNIST.

### Le logarithme naturel

*Répertoire : TP2_logarithme*

1.  Écrire un programme qui calcule la valeur de $e$ en utilisant la
série de Taylor, montrant la convergence de la série.

2.  Écrire un programme qui calcule le facteur (exprimé comme une
limite) dans la dérivé de $n^x$.

### Recommendation

*Répertoire : TP3_recommandation*

Utiliser le jeu de données MovieLens pour créer un moteur de
recommendation.

### CART

*Répertoire : TP4_CART*

Refaire MNIST avec une random forest et avec SVM (+rbf).  Faire une
comparaison des techniques : régression logistique (OvO, OvA), CART,
et SVM.

### CART, variation du 17 avril 2019

*Répertoire : TP4_CART++*

En cours le 17 avril 2019 nous allons regarder ensemble des jeux de
données
[ici](https://scikit-learn.org/stable/datasets/index.html#real-world-datasets).
Si vous voulez, vous pouvez les télécharger avant de venir au cours.
Vous le terminerez pour la semaine suivante.


## Étudiants

[Tanguy Badier](https://github.com/Rock3f/Exercice-Machine-Learning)

[Florian Boche](https://github.com/Nair0fl/CoursMachineLearning)

[Benjamin Brasseur](https://github.com/benjaminbra/ML-BBR)

[Clément Caillaud](https://github.com/ClementCaillaud/MachineLearning_ynov)

[Benoît Cochet](https://github.com/BenoitCochet/ML)

[Yanis Dando](https://github.com/Mokui/code_ML)

[Alexandre Desvallées](https://github.com/AlexDesvallees/Alex-ML)

[Antoine Drouard](https://github.com/Coblestone/ML-2019)

[Matthieu Fournier](https://github.com/LordInateur/ML_2019_matthieuf_exo)

[Guillaume Fourny](https://github.com/gfourny/Machine-Learning)

[Antoine Gosset](https://github.com/AntoineGOSSET/Machine-Learning)

[Nicolas Goureau](https://github.com/Killy85/MachineLearningExercises)

[Grégoire Meunier](https://github.com/Grigusky/ml_2019)

[Kevin Pautonnier](https://github.com/KevinPautonnier/MachineLearning.git)

[Thomas Pichard](https://github.com/thomaspich/MachineLearning)

[Matthieu Saint-Martin](https://github.com/msaintmartin/ml-exercises)


## Projets

Pour le projet final, vous vous composerez en groupe de deux (minimum)
à quatre (maximum) personnes afin de faire un projet que vous
présenterez vendredi 4 mai lors de la dernière séance.  Vous pouvez
travailler sur n'importe quel projet qui vous semble bon si le
professeur est d'accord.  Le projet par défaut est de construire un
système de reconnaissance de visage qui reconnaît les 18 personnes du
cours (y compris le prof).

Lors de votre présentation, vous devez expliquer ce que vous avez
fait, y compris son évolution.  Par exemple, vous devriez expliquer la
première version du système, comment vous l'avez mesuré, et comment
vous l'avez amélioré.

Attention à ne pas vous laisser distraire par l'interface humaine.
Une IH est une bonne idée, mais un projet qui maîtrise parfaitement le
ML sans UI appréciable serait beaucoup mieux noté que le contraire.

Le choix du projet doit être convenu avant la fin du week-end initial
(7 avril) sauf dérogation explicite.  Dans les premiers jours vous
devez créer un planning provisionnel de ce que vous compter faire (au
moins par semaine) avec des points de progrès clairement défini tel
que c'est possible d'évaluer s'ils sont achevés ou pas.

Quand vous achevez les points importants de progrès ou quand vous
auriez une question, vous devez créer un issue avec chacun dans
l'équipe ainsi que le professeur tagés afin que nous puissions
discuter votre progrès.


### [GATA](https://github.com/Rock3f/ML-Projet-GATA)
* Guillaume Fourny
* Alexandre Desvallées
* Tanguy Badier
* Antoine Gosset

Projet d'initiation à la reconnaissance faciale

### [Nikmabe](https://github.com/Killy85/game_ai_trainer) 
* Nicolas
* Benjamin
* Kevin
* Matthieu Fournier

Project aiming at creating a bot able to play a game the best way
possible.  Using reinforcement learning, we will create an agent and
make it learn our game.

