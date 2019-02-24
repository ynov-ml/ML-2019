# Machine Learning

Bienvenu au Machine Learning à Ynov !

Ce cours comportera un mixe de cours magistraux, de travaux dirigés en
présentielle, et de travaux et d'apprentissage par projet en
distancielle.  Les proportions seront établie entre le professeur et
les étudiants en vue de la capacité des étudiants à avancer dans le
sujet.

Ce document vous offre un aperçu préliminaire des pré-requis que vous
devez maîtriser avant le début du cours le 15 mars.  Ce sera mis à
jour progressivement d'ici le début mars.

En bref, vous devez avoir des compétences de bases dans les domaines
suivants :

* git
* python
* maths
  * algèbre linéaire
  * probabilité

Afin de bien préparer le premier jour du cours, pensez à envoyer un
mél au professeur, jeff.abrahamson@ynov, afin de partager avec lui
votre niveau et progrès dans ces sujets.  Cela nous permettra
également de mettre à jour ce document.


## Git

Impératif : add, commit, push, pull, diff, log, status, merge,
checkout, branch, ainsi que les options les plus communes de chaqu'un.

Recommandé : rebase (et rebase -i), mv, reset, cherry et cherry-pick,
ainsi que les options moins connues.

Vous comprenez bien entendu la différence entre l'outil git et le site
github...


## Python

Vous n'êtes pas obligé d'être pro en python, mais une connaissance de
base -- comment déclarer des fonctions, calculer les choses simples,
interagir avec les listes, les dicts, se servir des list et dict
comprehensions.  En plus, vous avez installé python et une poignée de
libraries sur votre (vos) ordinateur(s).  Voir outils et support,
ci-bas.


## Maths

En algèbre linéaire, vous n'avez pas peur des vecteurs et matrices.
Vous comprenez des opérations de bases : addition et multiplication.
Vous comprenez qu'une matrice représente une transformation en termes
d'une base donnée.

En probabilité, vous comprenez les conceptes de dépendances et
indépendances, la probabilité conditionnelle, et, idéallement, le
théorème de Bayes.

Nous vous proposerons quelques resources pour réviser ces sujets.


## Outils et support

Il est bien évidemment impératif que vous puissiez écrire et essayer
des programs en python.  Avant la première séance, il convient donc de
télécharger et installer python sur votre ordinateur.  La bonne
nouvelle, c'est que c'est gratuit et (selon votre système
d'exploitation) relativement simple.

### Linux

C'est un de rare cas dans la vie où tout est plus facile sur linux.
Afin, pour une certain définition de "facile".  Il suffit d'installer
python3 (attention : souvent python = python2) et virtualenv.
Virtualenv vous crée un environnement pour python largement
indépendant de ce qui est présent sur votre ordinateur.

Sur ubuntu, on peut taper

    $ sudo apt-get update
	$ sudo apt-get install python3-virtualenv virtualenv python python3
	$ sudo apt-get install gcc g++ python3-dev

Puis, dans votre répertoire de travail :

    $ virtualenv --python=python3 venv
	$ . venv/bin/activate                   # N'oubliez pas le "." au début.
	$ pip install -r requirements.txt

Le fichier `requirements.txt` se trouve [ici](requirements.txt).  Le
plus facile est de cloner ce repository.  Voir plus bas, "jour 1", sur
`git clone`.

Cela marche également sur MacOS si vous êtes à l'aise dans le terminal.

### MacOS, Windows

Apparemment l'usage de python sur Windows marche très bien sauf quand
ce n'est pas le cas.  Les systèmes MacOS et linux sont beaucoup plus
répandus dans le domaine de stat/ML/data science.  Ceci dit, un
produit commercial avec une très bonne offre gratuite existe :
[anaconda](https://www.anaconda.com/).  Il est téléchargeable
[ici](https://www.anaconda.com/download/).

### Tester

Vous avez sans doute le bon instinct de demander si vous avez bien
suivi cette démarche.  Vous pouvez lancer `ipython` (commandline:
ipython; sinon, il y a un icône quelque part).  Et puis vous devez
pouvoir faire le suivant :

	(venv) vagrant@ubuntu-bionic:~$ ipython
	Python 3.6.7 (default, Oct 22 2018, 11:32:17)
	Type 'copyright', 'credits' or 'license' for more information
	IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

	In [1]: import numpy as np

	In [2]: import scipy as sp

	In [3]: import sklearn

	In [4]: print("Hello, world!")
	Hello, world!

	In [5]: quit
	(venv) vagrant@ubuntu-bionic:~$

Il existe également une version du même logiciel qui vous présente un
éditeur dans votre browser : le Jupyter notebook.  Si vous l'essayez
sans browser, vous auriez ça :

	(venv) vagrant@ubuntu-bionic:~$ jupyter notebook

	[I 13:15:41.693 NotebookApp] Serving notebooks from local directory: /home/vagrant
	[I 13:15:41.693 NotebookApp] The Jupyter Notebook is running at:
	[I 13:15:41.693 NotebookApp] http://localhost:8888/?token=f949d83075275b57602064d7dc91c31b449009bd09a26f9e
	[I 13:15:41.693 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
	[W 13:15:41.697 NotebookApp] No web browser found: could not locate runnable browser.
	[C 13:15:41.697 NotebookApp]

		To access the notebook, open this file in a browser:
			file:///run/user/1000/jupyter/nbserver-8273-open.html
		Or copy and paste one of these URLs:
			http://localhost:8888/?token=f949d83075275b57602064d7dc91c31b449009bd09a26f9e
	^C[I 13:15:42.734 NotebookApp] interrupted
	Serving notebooks from local directory: /home/vagrant
	0 active kernels
	The Jupyter Notebook is running at:
	http://localhost:8888/?token=f949d83075275b57602064d7dc91c31b449009bd09a26f9e
	Shutdown this notebook server (y/[n])? ^C[C 13:15:42.890 NotebookApp] received signal 2, stopping
	[I 13:15:42.892 NotebookApp] Shutting down 0 kernels
	(venv) vagrant@ubuntu-bionic:~$

Avec un browser, vous verrez ouvrir une fenêtre.


