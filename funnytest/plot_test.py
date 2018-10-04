import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def tab():
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    return df


def hua():
    plt.plot([6, 6, 6, 6])
    plt.ylabel('some numbers')
    plt.show()


if __name__ == '__main__':
    df = tab()
    del df
