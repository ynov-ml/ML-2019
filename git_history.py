import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

def main():
    """Plot some git commits for practice.
    """
    r = requests.get('https://api.github.com/repos/JeffAbrahamson/dotfiles/stats/commit_activity')
    raw = r.text
    results = json.loads(raw)
    results
    df = pd.DataFrame(results)
    df.head()
    df['date'] = pd.to_datetime(df.week, unit='s')
    df.head()
    df['week_no'] = df.apply(lambda x: '{:d}-{:02d}'.format(x['date'].year,
                                                            x['date'].weekofyear),
                             axis=1)
    df.set_index('week_no')['total'].plot.bar()
    plt.show()

if __name__ == '__main__':
    main()
