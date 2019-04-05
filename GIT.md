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

[Matthieu Saint-Martin](https://github.com/msaintmartin/ml-exercises)

