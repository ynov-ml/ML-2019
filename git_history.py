#!/usr/bin/env python

import datetime
import git
import matplotlib.pyplot as plt
import numpy as np

def repo_get_commits(repo_name):
    """Get the commits in one repo, return a sorted array of commit timestamps.
    """
    repo = git.Repo(repo_name)
    # Use a set because branches often overlap.
    timestamps = set()
    for branch in repo.branches:
        for commit in branch.commit.iter_parents():
            timestamps.add(commit.authored_datetime)
    return sorted(list(timestamps))

def main():
    """Plot some git commits.
    """
    repo_names = ['alexandre-desvallées', 'antoine-drouard', 'antoine-gosset',
             'benjamin-brasseur', 'benoît-cochet', 'clément-caillaud',
             'florian-boche', 'grégoire-meunier', 'guillaume-fourny',
             'kevin-pautonnier', 'matthieu-fournier', 'matthieu-saint-martin',
             'maxime-courant', 'nicolas-goureau', 'projet-gata', 'projet-mymeteo',
             'projet-neuronal-gates', 'projet-nikmabe', 'tanguy-badier',
             'thomas-pichard', 'yanis-dando']
    time_series = []
    for repo_name in repo_names:
        time_series.append(repo_get_commits('/ML-2019-étudiants/' + repo_name))
    min_timestamp = min([min(series) for series in time_series])
    max_timestamp = max([max(series) for series in time_series])
    # Use two more than the days available to deal with times a bit
    # before or after first and last day.
    days_in_universe = (max_timestamp - min_timestamp).days + 2
    # Now I'd like each time series expressed as a sequence of floats
    # representing days since day 0.
    day_series = []
    for series in time_series:
        day_series.append([(d - min_timestamp).days + (d - min_timestamp).seconds / 3600. / 24.
                           for d in series])
    plt.xlim(0, days_in_universe)
    plt.xticks(np.arange(days_in_universe))
    plt.yticks(np.arange(len(repo_names)), repo_names)
    for index, series in enumerate(day_series):
        plt.scatter(series, [index] * len(series))
    plt.show()

if __name__ == '__main__':
    main()
